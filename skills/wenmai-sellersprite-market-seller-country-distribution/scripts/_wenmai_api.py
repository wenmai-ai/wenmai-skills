#!/usr/bin/env python3
"""Call one fixed Wenmai standard API endpoint for a self-contained Skill."""

import json
import os
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

DEFAULT_ORIGIN = "https://all-api.wenmai-ai.com"
BASE_PATH = "/wmapi/v1"
PERSONAL_CENTER_URL = "https://agent.wenmai-ai.com/"


def die(message: str, code: int = 1) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(code)


def load_params(script_name: str, sample_params: dict) -> dict:
    if len(sys.argv) != 2:
        example = json.dumps(sample_params, ensure_ascii=False)
        die(f"Usage: {script_name} '<JSON parameters>'\nExample: {script_name} '{example}'")
    try:
        params = json.loads(sys.argv[1])
    except json.JSONDecodeError as exc:
        die(f"Invalid JSON parameters at line {exc.lineno}, column {exc.colno}.")
    if not isinstance(params, dict):
        die("Parameters must be a JSON object.")
    return params


def require_api_key() -> str:
    key = os.environ.get("WENMAI_API_KEY") or os.environ.get("WENMAI_SECRET_KEY")
    if not key:
        die(
            "缺少 WENMAI_API_KEY（也兼容 WENMAI_SECRET_KEY）。请在 "
            + PERSONAL_CENTER_URL
            + " 获取 secret-key；额度不足时在同一入口充值。",
            code=2,
        )
    return key


def _field_value(params: dict, dotted_path: str):
    current = params
    for part in dotted_path.split("."):
        expects_array = part.endswith("[]")
        key = part[:-2] if expects_array else part
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
        if expects_array and not isinstance(current, list):
            return None
    return current


def validate_params(params: dict, required_fields: list[str]) -> None:
    missing = [
        field
        for field in required_fields
        if _field_value(params, field) is None or _field_value(params, field) == "" or _field_value(params, field) == []
    ]
    if missing:
        die("Missing required parameter(s): " + ", ".join(missing), code=2)


def read_timeout() -> int:
    raw = os.environ.get("WENMAI_API_TIMEOUT", "120")
    try:
        timeout = int(raw)
    except ValueError:
        die("WENMAI_API_TIMEOUT must be an integer number of seconds.", code=2)
    if timeout <= 0:
        die("WENMAI_API_TIMEOUT must be greater than 0.", code=2)
    return timeout


def build_url(path: str) -> str:
    origin = os.environ.get("WENMAI_API_ORIGIN", DEFAULT_ORIGIN).rstrip("/")
    if not origin.startswith(("https://", "http://")):
        die("WENMAI_API_ORIGIN must be an HTTP(S) origin.", code=2)
    return f"{origin}{BASE_PATH}/{path.strip('/')}"


def _sanitize(value: object, api_key: str) -> str:
    text = str(value).replace(api_key, "[REDACTED]")
    text = re.sub(
        r"""(?i)(["'](?:secret-key|authorization)["']\s*:\s*["'])"""
        r"""(?:bearer\s+|basic\s+)?[^"']*(["'])""",
        r"\1[REDACTED]\2",
        text,
    )
    text = re.sub(
        r"(?i)((?:secret-key|authorization)\s*[:=]\s*)"
        r"(?:bearer\s+|basic\s+)?[^\s,;}\]]+",
        r"\1[REDACTED]",
        text,
    )
    return text[:500]


def call_standard_api(*, params: dict, path: str, required_fields: list[str]) -> dict:
    api_key = require_api_key()
    validate_params(params, required_fields)
    request = Request(
        build_url(path),
        data=json.dumps(params, ensure_ascii=False).encode("utf-8"),
        method="POST",
        headers={
            "Content-Type": "application/json",
            "secret-key": api_key,
            "User-Agent": "Wenmai-AI-Skill/1.0",
        },
    )
    try:
        with urlopen(request, timeout=read_timeout()) as response:
            raw_body = response.read()
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace") if exc.fp else exc.reason
        die(f"Wenmai API HTTP {exc.code}: {_sanitize(detail, api_key)}")
    except URLError as exc:
        die(f"Wenmai API connection failed: {_sanitize(exc.reason, api_key)}")
    except TimeoutError:
        die("Wenmai API request timed out; check WENMAI_API_TIMEOUT and retry.")
    try:
        body = raw_body.decode("utf-8")
    except UnicodeDecodeError:
        die("Wenmai API returned a non-JSON response; no response body was logged.")
    try:
        result = json.loads(body)
    except json.JSONDecodeError:
        die("Wenmai API returned a non-JSON response; no response body was logged.")
    if not isinstance(result, dict):
        die("Wenmai API returned JSON with an unexpected top-level type.")
    return result


def run_api(*, script_name: str, path: str, required_fields: list[str], sample_params: dict) -> None:
    params = load_params(script_name, sample_params)
    result = call_standard_api(params=params, path=path, required_fields=required_fields)
    print(json.dumps(result, ensure_ascii=False, indent=2))
