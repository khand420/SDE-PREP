The correct answer to the question about which algorithm is best suited for finding all the strongly connected components in a directed graph is:

**Kosaraju’s Algorithm**

### Explanation:
- **Kosaraju's Algorithm** efficiently finds all strongly connected components (SCCs) in a directed graph using two depth-first searches (DFS). It first performs a DFS to determine the finishing order of nodes, then transposes the graph and performs another DFS based on the finishing order.

The other options are incorrect for the following reasons:
- **Dijkstra’s Algorithm**: This is used for finding the shortest paths from a source vertex to all other vertices in a weighted graph.
- **Kruskal’s Algorithm**: This algorithm is used for finding the minimum spanning tree in an undirected graph.
- **Floyd-Warshall Algorithm**: This algorithm is used for finding the shortest paths between all pairs of vertices in a weighted graph.



The correct answer to the question about which algorithm is used to find the maximum flow in a flow network is:

**Ford-Fulkerson Algorithm.**

### Explanation:
- The Ford-Fulkerson method is specifically designed to compute the maximum flow in a flow network. It uses augmenting paths to increase the flow until no more augmenting paths can be found.

The other options are incorrect for the following reasons:
- **Bellman-Ford Algorithm**: This algorithm is used for finding the shortest paths from a single source vertex to all other vertices in a graph, particularly with negative weight edges.
- **Floyd-Warshall Algorithm**: This algorithm finds the shortest paths between all pairs of vertices in a weighted graph.
- **Kruskal's Algorithm**: This algorithm is used for finding the minimum spanning tree of a graph, not for flow networks.

If you have more questions or need further clarification, feel free to ask!