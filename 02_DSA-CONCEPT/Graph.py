
def add_node(v):
    global node_count 
    if v in nodes:
        print(v, "is already present in the class")
    else:
        node_count = node_count+1
        nodes.append(v)
        for n in graph:
            n.append(0) 
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)  

def DeleteNode(v):
    global node_count 
    if v in nodes:
        print(v, "is not present in the class")
    else:
        index1 = nodes.index(v)
        node_count = node_count-1
        nodes.remove(index1)
        for i in graph:
            i.pop(index1)

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

def deleteEdge(v1, v2):
    if v1 not in nodes:
        print(v1, "Is not present in graph")
    elif v2 not in nodes:
        print(v2, "is not present in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0            


 
# 2. for Directed & Waited Graph
def add_edge(v1,v2, cost):
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")     
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index1] = cost
        graph[index2][index1] = cost

# # 3. for Directed & Un-Waited Graph
# def add_edge(v1,v2):
#     if v1 not in nodes:
#         print(v1, "is not present in the graph")
#     elif v2 not in nodes:
#         print(v2, "is not present in the graph")     
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index1] = 1
#        # # graph[index2][index1] = cost

# # 4. for un-Directed & Waited Graph
# def add_edge(v1,v2, cost):
#     if v1 not in nodes:
#         print(v1, "is not present in the graph")
#     elif v2 not in nodes:
#         print(v2, "is not present in the graph")     
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index1] = cost
       # # graph[index2][index1] = cost



def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],'<3'), end=" ")            
        print() 



nodes = []
graph = []
node_count = 0

print("Before adding nodes")
print("Node",nodes)
print('graph',graph)
add_node("A")
add_node("B")
add_node("D")
add_node("C")

# add_node("A")

# add_edge("A","B")
# add_edge("A","D")
add_edge("C","B", 5)
add_edge("A","D", 10)

print("After Adding Nodes")
print("Node",nodes)
print('graph',graph)

print("After Deleting Edge")
deleteEdge("A", "C")

print_graph()