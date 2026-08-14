def get_completion_signal_type(claim: AbsenceClaim) -> CompletionSignal.type:
    if claim.coverage_record:
        return CompletionSignal.type.COVERAGE
    else:
        return CompletionSignal.type.ABSENCE