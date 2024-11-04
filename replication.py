from hashing import get_node_for_key

def get_replica_nodes(key, nodes, num_replicas=2):
    primary_node = get_node_for_key(key, nodes)
    primary_index = nodes.index(primary_node)
    replica_nodes = [nodes[(primary_index + i) % len(nodes)] for i in range(num_replicas)]
    return replica_nodes
