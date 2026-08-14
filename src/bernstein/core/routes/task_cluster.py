def register_node(request: Request) -> Response:
    node_id = request.json['id']
    if node_id in cluster.nodes:
        node_info = cluster.nodes[node_id]
        node_info.hostname = request.json['hostname']
        node_info.capacity = request.json['capacity']
    else:
        node_info = NodeInfo(
            id=node_id,
            hostname=request.json['hostname'],
            capacity=request.json['capacity'],
        )
        cluster.nodes[node_id] = node_info
    node_register_request = NodeRegisterRequest(node_info=node_info)
    response = make_response(jsonify({'status': 'success'}), 200)
    return response