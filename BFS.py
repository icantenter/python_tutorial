graph = {"A": ["B", "C"],
         "B": ["A", "C", "D"],
         "C": ["A", "B", "D", "E"],
         "D": ["B", "C", "E", "F"],
         "E": ["C", "D"],
         "F": ["D"], }

def BFS(graph, start):
    queue = []
    queue.append(start)
    visited = set()
    visited.add(start)
    while queue:
        vertex = queue.pop(0)
        for node in graph[vertex]:
            if node not in visited:
                queue.append(node)
                visited.add(node)
        print(vertex)

BFS(graph, "E")

