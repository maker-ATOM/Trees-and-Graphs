"""
		     7
		   /   \
		  4     10
		 / \   /  \
		2   5 9   12
	   /			\
      1				13
"""

from tree import TreeNode, sample_binary_tree

def searchBST(node, val): 
    if node is None:
        return None

    result = TreeNode()

    if node.val == val:
        return node

    if val < node.val:
        result = searchBST(node.left, val)

    if val > node.val:
        result = searchBST(node.right, val)

    return result

if __name__ == '__main__':
    node = searchBST(sample_binary_tree, 4)

    try:
        node.print_BFS()
    except AttributeError:
        print("Number not Present")