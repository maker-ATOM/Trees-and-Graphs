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


def insertIntoBST(root, val):
    if root == None:
        return TreeNode(val)

    def helper(root, val):
        if root.left == None:
            if val < root.val:
                newNode = TreeNode(val)
                root.left = newNode
        
        if root.right == None:
            if val > root.val:
                newNode = TreeNode(val)
                root.right = newNode


        if val < root.val:
            insertIntoBST(root.left, val)

        if val > root.val:
            insertIntoBST(root.right, val)

    helper(root, val)
    return root

if __name__ == '__main__':
    insertIntoBST(sample_binary_tree, 11)
    sample_binary_tree.print_BFS()