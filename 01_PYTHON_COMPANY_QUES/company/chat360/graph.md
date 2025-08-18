Sure, let's implement a basic graph data structure in Python. We'll start by defining a `Graph` class, which will include methods for adding vertices and edges, as well as some additional methods for graph traversal and representation.

Here's a simple implementation:

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

# Example usage:
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')

print(graph)
```

### Explanation:

1. **Graph Class**: The `Graph` class contains a dictionary `self.vertices` where keys are vertices and values are lists of adjacent vertices (edges).

2. **add_vertex Method**: This method adds a vertex to the graph if it doesn't already exist.

3. **add_edge Method**: This method adds an edge between two vertices if both vertices exist in the graph. Since this example implements an undirected graph, the edge is added in both directions (from `vertex1` to `vertex2` and from `vertex2` to `vertex1`).

4. **__str__ Method**: This method provides a string representation of the graph, showing each vertex and its adjacent vertices.

### Example Output:
```
A -> ['B', 'C']
B -> ['A']
C -> ['A']
```

### Extending Functionality:
You can further extend this class to include methods for removing vertices and edges, performing graph traversal (like DFS and BFS), and other graph-related operations. Here's how you can add methods for removing vertices and edges:

```python
def remove_vertex(self, vertex):
    """Removes a vertex and all its edges from the graph."""
    if vertex in self.vertices:
        # Remove all edges to this vertex
        for other_vertex in self.vertices[vertex]:
            self.vertices[other_vertex].remove(vertex)
        # Remove the vertex
        del self.vertices[vertex]
    else:
        print(f"Vertex {vertex} not found in the graph.")

def remove_edge(self, vertex1, vertex2):
    """Removes an edge between vertex1 and vertex2."""
    if vertex1 in self.vertices and vertex2 in self.vertices:
        if vertex2 in self.vertices[vertex1]:
            self.vertices[vertex1].remove(vertex2)
        if vertex1 in self.vertices[vertex2]:
            self.vertices[vertex2].remove(vertex1)
    else:
        print("One or both vertices not found in the graph.")
```

You can add these methods to the `Graph` class to enable the removal of vertices and edges.