"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""
from collections import deque



"""
My solution:
start traversal for every node, for the node the visited do not start the traversal
after traversal update provinces
when a node is been chosen for traversal all it neighbors will be marked visited so a non-visited node indicates it is from a different province.
"""

def adjacency_matrix_to_list(adj_matrix):
    adj_list = []
    num_nodes = len(adj_matrix)

    for i in range(num_nodes):
        neighbors = []
        for j in range(num_nodes):
            if adj_matrix[i][j] == 1 and i + 1 != j + 1:  # Exclude self-connections
                neighbors.append(j + 1)  # Convert to 1-indexed
        adj_list.append(neighbors)

    return adj_list

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
adj = adjacency_matrix_to_list(isConnected)
print(adj)

provinces = []
visited = [False] * len(isConnected)

for i in range(1,len(isConnected) + 1):



    if not visited[i-1]:
        queue = deque([i])
        bfs = []


        while queue:

            node = queue.popleft()
            bfs.append(node)
            visited[node-1] = True

            for neighbor in adj[node-1]:
                if not visited[neighbor-1]:
                    queue.append(neighbor)
                    visited[neighbor-1] = True


        provinces.append(bfs)

print(f"Output: {len(provinces)}")


# GPT

"""
We use a set visited to track visited nodes.
We use a recursive DFS approach (dfs function) to traverse the graph.
We directly use the isConnected adjacency matrix for traversal without reconstructing the adjacency list.
We count the provinces by incrementing provinces when we encounter a new unvisited node.
"""

class Solution:
    def findCircleNum(self, isConnected) -> int:
        num_nodes = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(node):
            visited.add(node)
            for neighbor in range(num_nodes):
                if isConnected[node][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)

        for node in range(num_nodes):
            if node not in visited:
                provinces += 1
                dfs(node)

        return provinces