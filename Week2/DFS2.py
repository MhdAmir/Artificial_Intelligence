# Using a Python dictionary to act as an adjacency list
graph = {
  '1' : ['3','2'],
  '2' : ['4', '5'],
  '3' : ['6', '4'],
  '4' : ['6', '8', '7', '5'],
  '5' : ['7'],
  '6' : ['9', '8'],
  '7' : ['9'],
  '8' : ['9'],
  '9' : []
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
dfs(visited, graph, '1')