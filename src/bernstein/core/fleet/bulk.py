def dispatch_bulk_cost_report(args, extra_args=None):
    args = ['envelopes', 'estimate', 'policy', 'profile-report', *(extra_args or [])]
    # Register the command with the correct path
    # e.g., 'cost:envelopes:estimate:policy:profile-report'
    # Verify and keep consistent with the stated intent
    # For example, if the correct path is 'cost:envelopes:estimate:policy:profile-report',
    # replace the line above with:
    # args = ['cost', 'envelopes', 'estimate', 'policy', 'profile-report']