import hashlib
def get_node_for_key(key, nodes):
    hash_value = int(hashlib.sha256(key.encode()).hexdigest(), 16)
    return nodes[hash_value % len(nodes)]
