def parse_server_configs(config_dict):
    # ... existing code ...
    mcp_manager = MCPManager()
    mcp_manager.register_servers(config_dict)
    mcp_manager.register_with_config_gates()
    return mcp_manager.get_servers()

def validate_mcp_configs(config_dict):
    # ... existing code ...
    mcp_manager = MCPManager()
    mcp_manager.register_servers(config_dict)
    mcp_manager.register_with_config_gates()
    return mcp_manager.get_servers()
