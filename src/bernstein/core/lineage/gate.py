def check(self, write: Write, capability_delta: CapabilityDelta) -> bool:
    """Verify that a write was signed by an anchored identity and that the log bytes are canonical.

    Args:
        write: The write to verify.
        capability_delta: The capability delta to enforce.

    Returns:
        bool: True if the write is valid, False otherwise.
    """
    if not self._verify_signature(write):
        return False
    if not self._verify_canonical_log_bytes(write):
        return False
    if not self._enforce_capability_delta(write, capability_delta):
        return False
    return True

