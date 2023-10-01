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


def deleteNode(root, key):
    def findMin(node):
        while node.left:
            node = node.left
        return node

    if not root:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # Case 1 and Case 2: Node with one or no child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Case 3: Node with two children
        successor = findMin(root.right)
        root.val = successor.val
        root.right = deleteNode(root.right, successor.val)

    return root

if __name__ == '__main__':
    deleteNode(sample_binary_tree, 7)
    sample_binary_tree.print_BFS()