def register_node(request):
    node_id = request.json.get('node_id')
    if node_id and NodeInfo.exists(node_id):
        node_info = NodeInfo.get(node_id)
    else:
        node_info = NodeInfo(node_id=node_id)
    # ... rest of the function ...
