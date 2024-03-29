# Using a Python dictionary to act as an adjacency list
graph = {
  'A' : ['B','C'],
  'B' : ['H'],
  'C' : ['D', 'E'],
  'D' : ['F', 'G'],
  'E' : ['I'],
  'F' : ['H'],
  'G' : ['I'],
  'H' : ['I'],
  'I' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs
    if node not in visited:
        print (node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
          dfs(visited, graph, neighbour)


# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, 'A')