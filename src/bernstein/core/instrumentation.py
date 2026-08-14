def log_tool_call(self, call_id: str, tool: str, args: dict, success: bool, error: str, result: dict, coverage: dict) -> None:
    """Log a tool call to the tool-calls.jsonl file."""
    record = {
        "call_id": call_id,
        "tool": tool,
        "args": args,
        "success": success,
        "error": error,
        "result": result,
        "coverage": coverage
    }
    self._log_record(record)
