def register_node(request: Request) -> Response:
    node_info = NodeInfo(
        id=request.json['id'],
        hostname=request.json['hostname'],
        capacity=request.json['capacity'],
    )
    # Check if node already exists
    existing_node = get_node_by_id(node_info.id)
    if existing_node:
        # Update existing node's information
        existing_node.hostname = node_info.hostname
        existing_node.capacity = node_info.capacity
        response = handle_node_update_request(existing_node)
    else:
        # Register new node
        node_register_request = NodeRegisterRequest(node_info=node_info)
        response = handle_node_register_request(node_register_request)
    return Response(response)
