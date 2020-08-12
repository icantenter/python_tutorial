import heapq
import math

#图中的每条边都有权值，求一个点到另一个点的最短路径
graph = {"A": {"B": 5, "C": 1},
         "B": {"A": 5, "C": 2, "D": 1},
         "C": {"A": 1, "B": 2, "D": 4, "E": 8},
         "D": {"B": 1, "C": 4, "E": 3, "F": 6},
         "E": {"C": 8, "D": 3},
         "F": {"D": 6}, }

def init_distance(graph, start):
    distance = {start: 0}
    for vertex in graph:
        if vertex != start:
            distance[vertex] = math.inf
    return distance

def dijkstra(graph, start):
    pqueue = []
    heapq.heappush(pqueue, (0, start))
    visited = set()
    #存储路径上每个节点得父节点
    parent = {start: None}
    distance = init_distance(graph, start)
    while pqueue:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        visited.add(vertex)

        #graph[vertex][node]由图得结构可知, 代表一个可选的点
        for node in graph[vertex].keys():
            if node not in visited:
                #更新最小距离和最短路径
                if dist + graph[vertex][node] < distance[node]:
                    distance[node] = dist + graph[vertex][node]
                    parent[node] = vertex
                    heapq.heappush(pqueue, (distance[node], node))
    return parent, distance

parent, distance = dijkstra(graph, "A")
print(parent)
print(distance)
