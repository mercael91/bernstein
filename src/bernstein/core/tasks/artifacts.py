def _canonical_finding_bytes(finding: dict) -> bytes:
    # ... (rest of the function remains the same)
    # Add a check to ensure all required fields are present
    required_fields = ['id', 'name', 'description', 'preimage']
    for field in required_fields:
        if field not in finding:
            raise ValueError(f'Missing required field: {field}')
    # ... (rest of the function remains the same)
