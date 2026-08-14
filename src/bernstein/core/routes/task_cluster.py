def register_node(request):
    node_id = request.json.get('node_id')
    if node_id:
        existing_node = NodeInfo.query.filter_by(node_id=node_id).first()
        if existing_node:
            return jsonify({'message': 'Node already registered'}), 200
        node_info = NodeInfo(node_id=node_id)
    else:
        node_info = NodeInfo()
    # ... rest of the function ...
