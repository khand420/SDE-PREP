Sure! Below is an implementation of both Breadth-First Search (BFS) and Depth-First Search (DFS) for the `Graph` class we defined earlier.

### Breadth-First Search (BFS)
BFS explores the graph level by level, starting from the given start vertex.

### Depth-First Search (DFS)
DFS explores as far as possible along each branch before backtracking, starting from the given start vertex.

Here’s how you can implement these search methods:

```python
class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        """Adds a vertex to the graph."""
        if vertex not in self.vertices:
            self.vertices[vertex] = []
        else:
            print(f"Vertex {vertex} already exists.")
    
    def add_edge(self, vertex1, vertex2):
        """Adds an edge between vertex1 and vertex2."""
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)  # For undirected graph
        else:
            print("One or both vertices not found in the graph.")
    
    def __str__(self):
        """Returns a string representation of the graph."""
        result = ""
        for vertex, edges in self.vertices.items():
            result += f"{vertex} -> {edges}\n"
        return result

    def bfs(self, start_vertex):
        """Performs BFS and returns the order of visited vertices."""
        visited = set()
        queue = [start_vertex]
        bfs_order = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                bfs_order.append(vertex)
                queue.extend([v for v in self.vertices[vertex] if v not in visited])
        
        return bfs_order

    def dfs(self, start_vertex):
        """Performs DFS and returns the order of visited vertices."""
        visited = set()
        stack = [start_vertex]
        dfs_order = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                dfs_order.append(vertex)
                stack.extend([v for v in self.vertices[vertex] if v not in visited])
        
        return dfs_order

# Example usage:
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')

print("Graph:")
print(graph)

print("BFS:", graph.bfs('A'))
print("DFS:", graph.dfs('A'))
```

### Explanation:

1. **BFS Method**:
   - `bfs` starts from the `start_vertex`, initializes a `visited` set, a `queue` for BFS traversal, and a `bfs_order` list to keep track of the order of visited vertices.
   - It iterates through the queue, visiting each vertex and enqueuing its unvisited neighbors.

2. **DFS Method**:
   - `dfs` starts from the `start_vertex`, initializes a `visited` set, a `stack` for DFS traversal, and a `dfs_order` list to keep track of the order of visited vertices.
   - It iterates through the stack, visiting each vertex and pushing its unvisited neighbors onto the stack.

### Example Output:
```
Graph:
A -> ['B', 'C']
B -> ['A', 'D']
C -> ['A', 'D']
D -> ['B', 'C']

BFS: ['A', 'B', 'C', 'D']
DFS: ['A', 'C', 'D', 'B']
```

In this example, starting from vertex 'A':
- The BFS visits the vertices in the order: `['A', 'B', 'C', 'D']`.
- The DFS visits the vertices in the order: `['A', 'C', 'D', 'B']`.