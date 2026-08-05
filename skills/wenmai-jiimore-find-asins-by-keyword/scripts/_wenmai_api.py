#!/usr/bin/env python3
"""Shared standard Wenmai API caller for one self-contained Skill."""

import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

DEFAULT_ORIGIN = "https://all-api.wenmai-ai.com"
DEFAULT_BASE_PATH = "/wmapi/v1"


def die(message: str, code: int = 1) -> None:
    print(message, file=sys.stderr)
    sys.exit(code)


def load_params(script_name: str, sample_params: dict) -> dict:
    if len(sys.argv) < 2:
        example = json.dumps(sample_params, ensure_ascii=False)
        die(f"Usage: {script_name} '<JSON parameters>'\nExample: {script_name} '{example}'")
    try:
        params = json.loads(sys.argv[1])
    except json.JSONDecodeError as exc:
        die(f"Invalid JSON parameters: {exc}")
    if not isinstance(params, dict):
        die("Parameters must be a JSON object.")
    return params


def require_api_key() -> str:
    key = os.environ.get("WENMAI_API_KEY") or os.environ.get("WENMAI_SECRET_KEY")
    if not key:
        die(
            "缺少 WENMAI_API_KEY。请在 "
            "https://agent.wenmai-ai.com/app/account 的个人中心获取 secret-key，并导出为 WENMAI_API_KEY；"
            "额度不足时也在同一入口充值。"
            "示例：export WENMAI_API_KEY=sk-...",
            code=2,
        )
    return key


def _get_path(params: dict, path: str):
    current = params
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            return None
        current = current.get(part)
    return current


def validate_params(params: dict, required_fields: list[str]) -> None:
    missing = [name for name in required_fields if _get_path(params, name) in (None, "", [])]
    if missing:
        die("Missing required parameter(s): " + ", ".join(missing))


def read_timeout() -> int:
    raw = os.environ.get("WENMAI_API_TIMEOUT", "120")
    try:
        timeout = int(raw)
    except ValueError:
        die("WENMAI_API_TIMEOUT must be an integer number of seconds.")
    if timeout <= 0:
        die("WENMAI_API_TIMEOUT must be greater than 0.")
    return timeout


def build_url(path: str) -> str:
    origin = os.environ.get("WENMAI_API_ORIGIN") or os.environ.get("WENMAI_GATEWAY_ORIGIN", DEFAULT_ORIGIN)
    base_path = os.environ.get("WENMAI_API_BASE_PATH", DEFAULT_BASE_PATH)
    return f"{origin.rstrip('/')}/{base_path.strip('/')}/{path.strip('/')}"


def call_standard_api(*, params: dict, path: str, required_fields: list[str]) -> dict:
    api_key = require_api_key()
    validate_params(params, required_fields)

    data = json.dumps(params, ensure_ascii=False).encode("utf-8")
    request = Request(
        build_url(path),
        data=data,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "secret-key": api_key,
            "User-Agent": "Wenmai-AI-Skill/1.0",
        },
    )
    try:
        with urlopen(request, timeout=read_timeout()) as response:
            text = response.read().decode("utf-8")
            try:
                return json.loads(text)
            except json.JSONDecodeError:
                return {"raw": text}
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
        try:
            details = json.loads(body) if body else None
        except json.JSONDecodeError:
            details = body
        return {"error": "http_error", "status": exc.code, "reason": exc.reason, "details": details}
    except URLError as exc:
        return {"error": "connection_failed", "reason": str(exc.reason)}


def run_api(*, script_name: str, path: str, required_fields: list[str], sample_params: dict) -> None:
    params = load_params(script_name, sample_params)
    result = call_standard_api(params=params, path=path, required_fields=required_fields)
    print(json.dumps(result, ensure_ascii=False, indent=2))
