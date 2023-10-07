"""
Start from 0 and each node key is increasing from 0 to n (numeber of nodess)
"""

from typing import List
from collections import deque

class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        bfs = []  # List to store BFS traversal
        visited = [False] * V  # Initialize visited array
        queue = deque([0])  # Start BFS from node 0

        while queue:
            node = queue.popleft()
            bfs.append(node)
            visited[node] = True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

        return bfs
    
    def dfsOfGraph(self, V, adj):
        # code here
        visited = [False] * V
        dfslist = []
        
        def dfs(node):
            if visited[node]: return
            dfslist.append(node)
            visited[node] = True
            
            for neighnbours in adj[node]:
                dfs(neighnbours)
            
            
        dfs(0)
        return dfslist