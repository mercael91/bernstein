def _canonical_finding_bytes(finding: dict) -> bytes:
    # ... (rest of the function remains the same)
    # Add a check to ensure all fields are present in the finding
    if not all(field in finding for field in FINDING_FIELDS):
        raise ValueError('Missing required field')
