def get_model(self, decision_key):
    # A model must not be proposed unless the observed empirical confidence
    # meets the configured minimum. Compute it once and apply the gate to the
    # proposal returned by this method.
    empirical_confidence = self.empirical_confidence(decision_key)
    model = self._get_model(decision_key)

    if model is None or empirical_confidence < self.min_confidence:
        return None

    return model
