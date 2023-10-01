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


def isValidBST(root):
    result = []

    def preorderTrav(node):
        if node is None:
            return []

        if node.left is not None:
            preorderTrav(node.left)

        
        result.append(node.val)
        
        if node.right is not None:
            preorderTrav(node.right)

    preorderTrav(root)

    return all(result[i] < result[i+1] for i in range(len(result) - 1))

if __name__ == '__main__':
    print(isValidBST(sample_binary_tree))