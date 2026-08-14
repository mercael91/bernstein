def _extra_spawn_kwargs(self):
    kwargs = super().spawn_kwargs()
    kwargs['explicit_max_turns'] = self.max_turns
    return kwargs