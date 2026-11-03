#!/usr/bin/env python3
"""Request limits shared by the YY review scripts (see references/api.md)."""

from _wenmai_api import die

STATIONS = [str(i) for i in range(1, 21)]


def check_aids(params: dict) -> None:
    aids = params.get("aids")
    if not isinstance(aids, list) or not aids:
        die("aids must be a non-empty array of task ids (aid) returned by add_review_monitor_asins.py.")
    if len(aids) > 100:
        die(f"aids has {len(aids)} items; at most 100 per call. Split the ids into several calls.")
    if any(isinstance(aid, bool) or not isinstance(aid, int) for aid in aids):
        die("aids must contain integer task ids.")


def check_add(params: dict) -> None:
    asins = params.get("asins")
    if not isinstance(asins, list) or len(asins) != 1 or not isinstance(asins[0], str) or not asins[0].strip():
        die("asins must contain exactly 1 ASIN per call (billing is per requested page of that ASIN). "
            "Submit one call per ASIN.")
    pages = params.get("review_end_num")
    if pages is not None and (isinstance(pages, bool) or not isinstance(pages, int) or not 1 <= pages <= 10):
        die("review_end_num must be an integer from 1 to 10 (pages of 10 reviews each).")
