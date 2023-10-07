# Trees-and-Graphs

<p align="center">
	<b>Stack</b>
</p>
<p align="center">
	<img src="images/stack.png" width="495" height="276"/>
</p>

<p align="center">
	<b>Queue</b>
</p>
<p align="center">
	<img src="images/queue.png" width="730" height="304"/>
</p>


## Trees

<p align="center">
	<b>Tree</b>
</p>
<p align="center">
	<img src="images/tree.png" width="754" height="275"/>
</p>

```python
A tree is an undirected graph with no cycle.
A connected graph with N nodes and N - 1 edges.

```

<p align="center">
	<b>Rooting a Tree</b>
</p>
<p align="center">
	<img src="images/root.png" width="754" height="275"/>
</p>

```python
Rooted Tree => A tree with a designated root node with preferred directional edges.
```

**Storage methods**

```python
Edge list
    List of undirected edges indicating which two nodes have an between them.

Adjacency List
    Mapping of a node to all its neighbors

Adjacency Matrix

Flattened array => preferred for binary trees
    Where each node is assigned an index and the values are stored in an array with the indexes.

Trees can be non-directional as well.
```

## Binary Trees

<p align="center">
	<b>Binary Tree</b>
</p>
<p align="center">
	<img src="images/binary.png" width="754" height="275"/>
</p>

```python
Every Nodes has at most two child nodes.

Leaf Node => Lowest node with the tree  (Node with no children)

Height => Number of edges from the root node of leaf node.

Parent of root node is NIL

DataType: Set based Collection

Abilities:
    insert
    delete
    find
    traversal
        map
        iter

Each node has a key (value of node) associated so that it can be referenced and can be used for comparison.

Successor of a node N:
    The node with the smallest key greater than N's key.
    i.e move one step to right and then all the way to leftmost leaf.

```

<p align="center">
	<b>Binary Search Tree</b>
</p>
<p align="center">
	<img src="images/bst.png" width="754" height="257"/>
</p>

```python

Binary Search Tree => an variant of BT where the value of left node is less than 
and value of right node is greater than the value of current node.

Bad BST => when height of tree is same as number of nodes

    1
     \
      2
       \
        3
         .
          .
           n
       
Good BST => A well balanced tree, where height is equal to log_2(nodes)


		     7
		   /   \
		  4     10
		 / \   /  \
		2   5 9   12

```

### Traversal

Can be performed iteratively or recursively. Iterative approach uses stack to store the node to be visited.

**Depth First Search(preferred)**

```python
Easily implemented recursively
```

```python
Inorder
    Traverse the left subtree
    Visit the parent
    Traverse the right subtree

Preorder
    Visit parent
    Traverse the left subtree
    Traverse the right subtree

Postorder
    Traverse the left subtree
    Traverse the right subtree
    Visit parent

BST when traversed in an inorder manner return a sorted array.
    Can be used to verify the validity of the tree.
```

**Breadth First Search**

```python
Traverse all the nodes of a lower level before moving to any of the nodes of a higher level.
```

```python
Naive approach
    Find height of tree. Then for each level, run a recursive function by maintaining current height. 
    Whenever the level of a node matches, use that node.

Queue
    Push the nodes of a lower level in the queue. When any node is visited, 
    pop that node from the queue and push the child of that node in the queue.

    Useful to find the height of the tree.
```

### Common Tree Problems

**Lowest Common Ancestor**

```python
check whether the nodes p and q are in the left and right subtrees of the current node,
and if so, returns the current node as the lowest common ancestor. Otherwise, 
it recursively searches in either the left or right subtree based on the presence of nodes p and q.

Pseudocode:

function lowestCommonAncestor(root, p, q):
    if root is None:
        return None
    
    # If either p or q matches the root value, it is the LCA
    if root == p or root == q:
        return root
    
    # Recur for left and right subtrees
    left_lca = lowestCommonAncestor(root.left, p, q)
    right_lca = lowestCommonAncestor(root.right, p, q)
    
    # If both nodes are found in the left and right subtrees, then the current node is the LCA
    if left_lca and right_lca:
        return root
    
    # Otherwise, return the non-None node (either left_lca or right_lca)
    return left_lca if left_lca else right_lca

```
**Binary Tree From Preorder**

**Recovery of Binary Tree**

**Rooting a Tree**

### Operations

**Validity**
```python
A tree is binary search tree or not can checked by utilizing the property that inorder traversal
 generates a sorted list. If it is not then three is not a valid BST
```
**Height**
```python
The height of the tree can figured out by measuring the levels of traversal in BFS.
```

**Insert**
```python
Insertion can be performed by utilizing DFS and attaching a new node at the appropriate leaf node.
```

**Delete**
```python
For deletion different cases needs to considered.
    Node with no children (Leaf node): Simply remove the node.
    Node with one child: Replace the node with its child.
    Node with two children: Find the node's in-order successor (smallest node in its right subtree), 
    copy the successor's value to the node, and then delete the successor.
```

## Self Balancing Trees

```python
Trees which optimize their structure so that the height of the tree is as low as possible.
```

### Red-Black Trees

BST + "stuff"

```python
Every node has color, red or black (single bit data) associated

Rules:
    The root and leaves are colored black.
    Every red node must have 2 black children.
    ❗ The number of black nodes on any path from any node to its leaf must be same.

Example: ○ - black, ● - red

           ○
       /        \
      ●          ○
   /     \        \
  ○       ○        ●
 / \    /   \     / \
○   ○  ●     ●   ○   ○
      / \   / \  
     ○   ○ ○   ○   

Height of a red-black tree (h)
log_2(n) < h < 2(log_2(n)) , where n is number of nodes
```

[Treaps](https://www.youtube.com/watch?v=d0rlrRZc-0s)

## Skip List

Alternative to balance trees.
Randomized data structure uses probability.

```python
A combination of list stacked on top of each other where bottom list contains all the element 
as we go up of the list only the important elements are kept and others are skipped.

Each layer is a subset of layer below.
Bottom layer contains all the elements.
Each layer is sorted
And two pointers are used, right  - indicating to next element in same layer.
                           bottom - indicating to same element in the below layer.

Start from top left elements go right until required element is greater that current element
Move down if next element is greater that required element, repeat the process.

When a element is to be inserted it is first added in the bottom most layer then a coin is tossed
to decide whether the node is to be added in the top layer or not, making it a probabilistic data structure. 
```

---

## Graphs

<p align="center">
	<b>Undirected graphs</b>
</p>

```python
Edges have no orientation (direction)
```


<p align="center">
	<img src="images/undirected.png" width="730" height="304"/>
</p>


<p align="center">
	<b>Directed graphs</b>
</p>

```python
Edges have orientation (direction). Traversal happens in the indicated direction only and not the other way around.
```


<p align="center">
	<img src="images/directed.png" width="730" height="304"/>
</p>

<p align="center">
	<b>Weighted Graphs</b>
</p>


```python
Where edges have weights associated which connects nodes.
```


<p align="center">
	<img src="images/weighted.png" width="730" height="304"/>
</p>

<p align="center">
	<b>Directed Acyclic graphs</b>
</p>


```python
Directed graphs with no cycles.
```


<p align="center">
	<img src="images/directedacyclic.png" width="890" height="271"/>
</p>

**Storage methods**
```python
- Adjacency 2D matrix.
- Adjacency Lists.
- Edge list.
```

### Traversal

**Depth First Search**

```python
Plunges depth first into into a graph without regard for which edge it take next
until it cannot go further at which point it backtracks and continues.

We do not revisit a node. This happens in case of cycle, so
So we backtrack to the cycle origin and continue.

Usage:
    - Used to find number of components within a graph by assigning ids to each group.
    - Compute a graphs minimum spanning tree
    - Detect and find cycles
    - Check if a graph is a bipartite
    - Find strongly connected components.
    - Topologically sort the nodes of a graph.
    - Find bridges and articulation points.
    - Find augmented paths in a flow network.
    - Generate mazes.
```

[Visualization](https://www.youtube.com/watch?v=NUgMa5coCoE)

**Breadth First Search**

```python
Explores the neighbor nodes first, before moving to the next level of neighbors.
Utilizes queue to store the node yet to be visited

usage:
    - Shortest path on unweighted graphs.
```

[Visualization](https://www.youtube.com/watch?v=x-VTfcmrLEQ)

### Common Graph Theory Problems

```python
Askable questions:
- Is the graph directed or undirected?
- Are the edges of the graph weighted?
- Is  the graph dense with edges?
- What data structure should I use for representation of matrix?
```

```python
Shortest path from Node A to Node B. in a weighted graph.
- Algos: BFS (unweighted graph), Dijkstra's, Bellman-Ford, A* 

Connectivity between two Node
- Solution: Search operation.

Negative cycles
- Algos: Bellman-Ford, Floyd-Warshall

Strongly Connected Components
- Algos: Tarjans' and Kosaraju's

**Traveling Sales Person**
- Algos: Held-Karp, branch and bound.

Bridges

Minimal Spanning Trees
- Algos: Krushal's, Prims's, 

Network Flow
- Algos: Ford-Fulkerson.

Identification of cycles
```
**BFS on Grids**

```python
```

## Resource


[Resource](https://www.youtube.com/watch?v=44TwrxjfIfo&list=PLDV1Zeh2NRsCmu1lb9grUcljeYJtmgmYc)
