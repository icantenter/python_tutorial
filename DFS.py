graph = {"A": ["B", "C"],
         "B": ["A", "C", "D"],
         "C": ["A", "B", "D", "E"],
         "D": ["B", "C", "E", "F"],
         "E": ["C", "D"],
         "F": ["D"], }

def BFS(graph, start):
    stack = []
    stack.append(start)
    visited = set()
    visited.add(start)
    while stack:
        vertex = stack.pop()
        for node in graph[vertex]:
            if node not in visited:
                stack.append(node)
                visited.add(node)
        print(vertex)

BFS(graph, "A")
