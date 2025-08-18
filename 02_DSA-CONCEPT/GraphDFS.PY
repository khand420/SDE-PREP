def add_node(v):
    if v in graph:
        print(v, "is already present in graph")
    else:
        graph[v] = []    


# # 1. for Un-Directed & Un-Waited Graph
def add_edge(v1,v2):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")   
    else:
        # list1 = [v2.cost]
        # list2 = [v2.cost]
        graph[v1].append(v2)
        graph[v2].append(v1)     


def deleteNode(v):
    if v not in graph:
        print(v, "is not present in the graph")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            for j in list1:
                if v == j[0]:
                    list1.remove(j)
                    break  


# # 1. for Un-Directed & Un-Waited Graph
# def add_edge(v1,v2):
#     if v1 not in nodes:
#         print(v1, "is not present in the graph")
#     elif v2 not in nodes:
#         print(v2, "is not present in the graph")     
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index1] = 1
#         graph[index2][index1] = 1


def DFS(node,visited, graph):
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i, visited, graph)


def DFS_Recursive(node,visited, graph):
    if node not in visited:
        print("Node is not present in the graph!")
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i, visited, graph)

def DFS_Iterative(node, graph):
    visited = set()
    if node not in visited:
        print("Node is not present in the graph!")
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)


visited = set()
graph= {}

add_node("A")
add_node("B")
add_node("D")
add_node("E")
add_node("C")

add_edge("C","B")
add_edge("A","D")
add_edge("B","E")
add_edge("A","C")
add_edge("A","B")
add_edge("A","B")
add_edge("E","D")
add_edge("C","D")

# print_graph()

# DFS("B",visited, graph)
# DFS_Recursive("B",visited, graph)
DFS_Iterative("A", graph)


# deleteNode("A")