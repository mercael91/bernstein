def register_node(request: Request) -> Response:
    try:
        node_id = request.json['id']
        hostname = request.json['hostname']
        capacity = request.json['capacity']
    except KeyError as e:
        return Response(status=400, body=f"Missing required field: {e}")

    if not all(isinstance(field, str) for field in [node_id, hostname]) or not isinstance(capacity, int):
        return Response(status=400, body="Invalid data types")

    node_info = NodeInfo(
        id=node_id,
        hostname=hostname,
        capacity=capacity,
    )

    if node_info.id in registered_nodes:
        return Response(status=200)

    node_register_request = NodeRegisterRequest(node_info=node_info)
    registered_nodes[node_info.id] = node_info
    return Response(status=200)
