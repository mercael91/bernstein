def register_node(request: Request) -> Response:
    try:
        node_info = NodeInfo(
            id=request.json['id'],
            hostname=request.json['hostname'],
            capacity=request.json['capacity'],
        )
        if node_info.id in cluster.nodes:
            # Node already exists, update its information
            cluster.nodes[node_info.id] = node_info
            return Response({'status': 'success', 'message': 'Node information updated'})
        else:
            # New node, register it
            cluster.nodes[node_info.id] = node_info
            return Response({'status': 'success', 'message': 'Node registered'})
    except KeyError as e:
        return Response({'status': 'error', 'message': f'Missing required field: {e}'}, status=400)
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=500)
