import sys

def find_augmenting_path(adjacents, start, end, path=[1]):
    # DFS
    if start == end:
        return path
    for i in range(len(adjacents[start])):
        if adjacents[start][i] > 0 and i not in path:
            new_path = find_augmenting_path(adjacents, i, end, path + [i])
            if new_path:
                return new_path
    return None

def find_min(path, adjacents):
    min_val = float('inf')
    for i in range(len(path) - 1):
        if adjacents[path[i]][path[i+1]] < min_val:
            min_val = adjacents[path[i]][path[i+1]]
    return min_val

def update_flow(flow_graph, adjacents, path, val):
    for i in range(len(path) - 1):
        flow_graph[path[i]][path[i+1]] += val
        adjacents[path[i+1]][path[i]] += val
        adjacents[path[i]][path[i+1]] -= val

for _ in range(int(sys.stdin.readline())):
    data = sys.stdin.readline().split()
    num_nodes = int(data[0])
    num_edges = int(data[1])
    flow = [[0] * (num_nodes + 1) for _ in range(num_nodes + 1)]
    adjacents = [[0] * (num_nodes + 1) for _ in range(num_nodes + 1)]
    
    for __ in range(num_edges):
        line = sys.stdin.readline().split()
        u = int(line[0])
        v = int(line[1])
        capacity = int(line[2])
        adjacents[u][v] += capacity
    
    path = find_augmenting_path(adjacents, 1, num_nodes)
    max_flow = 0
    
    while path:
        min_flow = find_min(path, adjacents)
        max_flow += min_flow
        update_flow(flow, adjacents, path, min_flow)
        path = find_augmenting_path(adjacents, 1, num_nodes)
    print(max_flow)
