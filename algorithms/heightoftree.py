"""
     1
   /   \
  2     3
 / \   / \
4   5 6   7

"""

from tree import sample_binary_tree

def maxDepth_BFS(node):
    if not node:
        return 0
    
    queue = [node]
    next_queue = []
    level = []
    depth = 0
    
    while queue:
        for node in queue:
            level.append(node.val)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        depth += 1
        level = []
        queue = next_queue
        next_queue = []
    
    return(depth)

def maxDepth_DFS(node):
    def dfs(node, depth):
        if not node: return depth
        return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
                    
    return dfs(node, 0)

if __name__ == '__main__':
    print(maxDepth_BFS(sample_binary_tree))
    print(maxDepth_DFS(sample_binary_tree))

