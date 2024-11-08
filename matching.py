def find_augmenting_path(adjacents, start, end, path, visited):
    if start == end:
        return path
    visited.add(start)
    for i in adjacents[start]:
        if adjacents[start][i] > 0 and i not in visited:
            new_path = find_augmenting_path(adjacents, i, end, path + [i], visited)
            if new_path:
                return new_path
    return None

def update_flow(flow_graph, adjacents, path):
    for i in range(len(path) - 1):
        u, v = path[i], path[i+1]
        adjacents[u][v] -= 1
        if u not in adjacents[v]:
            adjacents[v][u] = 0
        adjacents[v][u] += 1

def main():
    test_cases = int(input())
    output = []
    for _ in range(test_cases):
        nodes_A, nodes_B, num_edges = map(int, input().split())
        num_nodes = nodes_A + nodes_B
        if num_edges == 0 or nodes_A == 0 or nodes_B == 0:
            print('0 N')
            continue
        flow = {i: {} for i in range(num_nodes + 2)}
        adjacents = {i: {} for i in range(num_nodes + 2)}
        for i in range(1, nodes_A + 1):
            adjacents[0][i] = 1
        for j in range(nodes_A + 1, num_nodes + 1):
            adjacents[j][num_nodes+1] = 1
        
        for __ in range(num_edges):
            u, v = map(int, input().split())
            adjacents[u][v + nodes_A] = 1
    
        path = find_augmenting_path(adjacents, 0, num_nodes + 1, [0], set())
        max_flow = 0
        
        while path:
            max_flow += 1
            update_flow(flow, adjacents, path)
            path = find_augmenting_path(adjacents, 0, num_nodes + 1, [0], set())
        if max_flow == min(nodes_A, nodes_B):
            output.append(str(max_flow) + ' Y')
        else:
            output.append(str(max_flow) + ' N')

    print('\n'.join(output))

if __name__ == "__main__":
    main()