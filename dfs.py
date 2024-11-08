import sys

def get_matrix(graph):
    matrix = {}
    for line in graph:
        nodes = line.split()
        adjacent_nodes = []
        for i in range(1, len(nodes)):
            adjacent_nodes.append(nodes[i])
        matrix[nodes[0]] = adjacent_nodes
    return matrix

def find_depth(start_node, input, visited, s):
    for node in input[start_node]:
        if node in visited:
            continue
        else:
            visited.append(node)
            find_depth(node, input, visited, s)

input = sys.stdin.readlines()
num_instances = int(input[0].strip())
line_num = 1
new_nodes = []

for _ in range(num_instances):
    num_nodes = int(input[line_num].strip())
    line_num += 1
    visited = []
    graph = input[line_num:line_num + num_nodes]
    adjacent_matrix = get_matrix(graph)
    for line in range(num_nodes):
        next_line = input[line_num].strip()
        line_num += 1
        new_nodes = next_line.split()
        if new_nodes[0] in visited:
            continue
        else:
            visited.append(new_nodes[0])
            find_depth(new_nodes[0], adjacent_matrix, visited, '')
    s = ''
    for i in range(len(visited) - 1):
        s += visited[i] + ' '
    s += visited[len(visited) - 1]
    print(s)
