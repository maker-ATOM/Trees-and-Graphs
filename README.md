<!-- 
Playlist status

11
12
13
14

17
18
19
20
21
22

24
25
26
27
28
29

33
34
35
36
37
38
39
40
41
42
43
 -->

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



# Trees

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

# Graphs

<p align="center">
	<b>Undirected graphs</b>
</p>

```python
Edges have no orientation (direction)
```


<p align="center">
	<img src="images/undirected.png" width="856" height="363"/>
</p>


<p align="center">
	<b>Directed graphs</b>
</p>

```python
Edges have orientation (direction). Traversal happens in the indicated direction only and not the other way around.
```


<p align="center">
	<img src="images/directed.png" width="856" height="331"/>
</p>

<p align="center">
	<b>Weighted Graphs</b>
</p>


```python
Where edges have weights associated which connects nodes.
```


<p align="center">
	<img src="images/weighted.png" width="856" height="331"/>
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

Reverse of a graph is a graph where the direction all the directed edges are reversed. If a graph is denoted by Adjacency 2D matrix the reverse of it is simply the transpose of the matrix. 

## Traversal

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

Utilizes recursive method to traverse the neighbor node of the current node.


Algorithm:

def bfsOfGraph(V,adj):
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
```

```python
Complexity: O(V+E)
```

[Visualization](https://www.youtube.com/watch?v=NUgMa5coCoE)

One of the traversal aspect is the discovery and finish time.
Discovery time is the time stamp from the start of the traversal when the node is marked visited and finish time is the time stamp where the there are no more neighbors of the node and the is never going to be visited.
Each jump from a node to another results in increment in time.

**Breadth First Search**

```python
Explores the neighbor nodes first, before moving to the next level of neighbors.
Utilizes queue to store the node yet to be visited

usage:
    - Shortest path on unweighted graphs.

Utilizes queue to store the next node should be visited next.

Algorithm:

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
```

```python
Complexity: O(V+E)
```

[Visualization](https://www.youtube.com/watch?v=x-VTfcmrLEQ)

## Common Graph Theory Problems

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
A grid can be easily converted to a Adjacency list.
    - LAbel each cell with numbers, each cell denotes a node.
    - Neighboring cells are ones connected up, down, left and right

A grid if represented using a 2D matrix (x,y) in that senario we do not need to
generate a Adjacency list, adjacent elements are can evaluated by adding a direction vector.
and then checking if the generated cell is a valid cell or not.
If it is enqueue it for next iteration and mark it as visited.

If the path is to be drawn from start to end we need to store 
the previously visited node for each current node.
```

**Topological Sort**

<p align="center">
	<img src="images/topsort.png" width="890" height="271"/>
</p>

```python
A topological ordering is an ordering of the nodes in a directed edge from node A to B, 
where node A appears before node B in the ordering.

Topological ordering are NOT unique. 

A graph with cycle cannot have a valid ordering.
Only Directed Acyclic Graphs have valid topological ordering.
How to find if a graph contains cycle or not?
    Tarjan's strongly connected components.

All trees have topological ordering which is the BFS traversal of the tree.

Algorithm:
    Pick an unvisited node.
    Beginning with the selected node, da a DFS exploring only unvisited nodes.
    On recursive callback of DFS, add the current node to the topological ordering in reverse order.

Kahn's Algorithm
    Detects if a graphs contains a cycle or not. 

    Repeatedly remove nodes without any dependencies from the graph and add them to the topological ordering.
    As nodes without dependencies (and their outgoing edges) are removed from the graph, 
    new nodes without dependencies should become free.
    We repeat removing nodes without dependencies from the graph until all nodes are processed, 
    or a cycle is discovered. 

    Dependencies can be found out from the Adjacency list or matrix.
```

```python
Complexity: O(V+E)
```

**Strongly connected components (SCC)**

<p align="center">
	<img src="images/scc.png" width="987" height="362"/>
</p>

```python
Strongly connected components can thought of as self-contained cycles within a directed graph where
every vertex in a given cycle can reach every other vertex of the same cycle. 
More or else it is a group of nodes within the graph where each node can be reached from every other node.

Low-Link Value:
    The low-link value of a node is the smallest (lowest) node id reachable from that node when doing a DFS (including itself)
When assigned low link values to the nodes traversed in DFS in turns out to be that all strongly connected components have same low link value.
But this depends on the start node of DFS which is random.

This is where tarjan's algo come in handy.

Tarjan's Algorithm:
    Mark the id of each node as unvisited.
    Start DFS. Upon visiting a node assign it an id and a low-link value. 
        Also mark current nodes as visited and add them to a seen stack.
    On DFS callback if the prev node is on stack then min the current node's low link value with the last node's low link value. 
        (This allows low link values to propagate through cycles)
    After visiting all neighbors, if the current node started a connected component
        (a node starts a connected component if its id is equal to its low link value) 
            then pop nodes off stack until current node is reached.

Maximal strongly connected components are ones which cannot be extended into SCC by adding other nodes.
Properties:
    Intersection of all MSCC is a null set.
    If we combine all SCC into a single node then the super-graph generated is a directed acyclic graph

SCC can also be figured out by performing DFS on the reverse graph and generating a list of completed cycles.
```

```python
Complexity: linear O(V+E)
```

**Amortized Analysis**

```python
Technique for analyzing cost of operations.
```

**Minimal Spanning Tree (MST)**

<p align="center">
	<img src="images/mst.png" width="840" height="483"/>
</p>

```python
A minimum spanning tree is a subset of the edges in the graph which connects all vertices together, 
without creating any cycle while minimizing the total edge cost.
A graph can have multiple MST with same costs.
MST are not unique.
All the nodes must be connected to form a spanning tree.
Can be used to find the minimum cost required to reach from one node to other.
Technically we drop edges with higher weights.

Example: nodes can be servers and weighted edges can be speed of transmission.

Prim's Algorithm
    Greedy Algorithm
    Difficult to find MST on disconnected components using this algo.

    Maintain a min Priority Queue (PQ) that sorts edges based on min edge cost. 
    This will be used to determine the next node to visit and the edge used to get there.
    Start the algorithm on any node s. Mark s as visited and iterate over all edges of s, adding them to the PQ.
    While the PQ is not empty and a MST has not been formed, dequeue the next cheapest edge from the PQ.
    If the dequeued edge is outdated (meaning the node it points to has already been visited) then skip it and poll again.
    Otherwise, mark the current node as visited and add the selected edge to the MST.
    Iterate over the new current node's edges and add all its edges to the PQ. Do not add edges to the PQ which point to already visited nodes.

    The algorithm can be stopped when number of edges are one less than number of nodes as this is one of the definition of trees.

    Usually for this algo the graph is represented as adjacency list with all undirected edges as
    two directed edges. As the graph becomes dense adjacency matrix is preferred over list.

    As an upgrade we can avoid adding edges in the PQ which can become stale

    Complexity: O(E * log(E))

Eager Prim's
    Tracks (node, edge) key value pairs that can easily be updated and polled to determine the next best edge to add in MST.
    Instead of adding edges to the PQ as we iterate over the edges of node, we are going to update 
    the destination node's most promising incoming edge. 

    Complexity: O(E * log(V))

Kruskal's Algorithm
    Greedy
    Intermediate state is not a tree but a forest which we try to connect at the end.

    Sort the edges in ascending order.
    If an edge connects two different trees in an forest add it and make a single tree. 

    Complexitiy:  O(E * log(V))
```

### Union Find Data Structure 

Useful to find Minimal Spanning Tree

**Family of Disjoint Sets**

```python
e.g U = {1,2,3,4,5,6}
S1 = {1,2}, S2 = {2,4,5}, s3 = {6}
Intersection of all member in Null

Operations:

MakeSet => create a new set
Find    => return the representative of the set in which the element is
Union   => merger two or more sets

The set are presented by reverse tree. And the representative of the set is the root of the tree.
Note the tree is not binary so a node can have multiple children.
Rank is the longest path to leaf

The root with bigger rank of the tree becomes the representative while performing Union.
this reduces the depth of tree after multiple Union operations
```


## Resource


[William Fiset](https://www.youtube.com/watch?v=44TwrxjfIfo&list=PLDV1Zeh2NRsCmu1lb9grUcljeYJtmgmYc)
