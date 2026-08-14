"""Disposition tracking for review findings.

Wires review finding outcomes into empirical_confidence.record_outcome()
so each rule accumulates a precision history; rules with persistently
high dismiss/ignore rates become identifiable and retirable.
"""
from __future__ import annotations

from enum import Enum

from bernstein.core.quality.empirical_confidence import record_outcome


class Disposition(str, Enum):
    FIXED = "fixed"
    DISMISSED = "dismissed"
    IGNORED = "ignored"


def record_finding_disposition(rule_id: str, disposition: Disposition) -> None:
    """Record the disposition of a review finding for a given rule.

    Args:
        rule_id: Identifier of the rule that produced the finding.
        disposition: How the finding was resolved.
    """
    positive = disposition is Disposition.FIXED
    record_outcome(rule_id, positive=positive)
