def _extra_spawn_kwargs(self, task: Task) -> Dict[str, Any]:
    kwargs = {}
    if "explicit_max_turns" in inspect.signature(self.adapter.spawn).parameters:
        kwargs["explicit_max_turns"] = task.max_turns
    return kwargs