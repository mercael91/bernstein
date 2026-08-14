def record_outcome(self, outcome, min_samples=5):
    if min_samples > len(self.data):
        return Confidence(insufficient_data=True)
    # ... rest of the method implementation ...