def record_capability_delta(delta: CapabilityDelta) -> None:
    """Record a computed capability delta as an authenticated audit-chain event."""
    _record_event("capability_delta", delta)

