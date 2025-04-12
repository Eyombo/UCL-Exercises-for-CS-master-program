
graph = {
    0: [1, 3],
    1: [2],
    2: [0],
    3: [4],
    4:[3],
}
# Recursive DFS function
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set
    visited.add(node)    # Mark the node as visited
    print(node)          # Print the current node to the console
    for node in graph[node]:  # iterates through each neighbor of the current note
        if node not in visited:
            dfs_recursive(graph, node, visited)

dfs_recursive(graph, 0)