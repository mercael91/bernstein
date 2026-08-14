def register_node(request: Request) -> Response:
    node_info = NodeInfo(
        id=request.json['id'],
        hostname=request.json['hostname'],
        capacity=request.json['capacity'],
    )
    if node_info.id in registered_nodes:
        return Response(status=200)
    node_register_request = NodeRegisterRequest(node_info=node_info)
    registered_nodes[node_info.id] = node_info
    return Response(status=200)
