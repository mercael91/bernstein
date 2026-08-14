def confidence(agent_type, decision_key):
    empirical_confidence_value = empirical_confidence(agent_type, decision_key)
    if empirical_confidence_value < MIN_CONFIDENCE:
        return None
    # rest of the function remains the same