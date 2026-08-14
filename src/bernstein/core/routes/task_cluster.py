def register_node(request: Request) -> Response:
    try:
        node_info = NodeInfo(
            id=request.json['id'],
            hostname=request.json['hostname'],
            capacity=request.json['capacity'],
        )
    except KeyError as e:
        return Response({'error': f'Missing required field: {e}'}, status=400)

    try:
        node_register_request = NodeRegisterRequest(node_info=node_info)
        response = grpc_client.register_node(node_register_request)
        return Response(response.json(), status=response.status_code)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
