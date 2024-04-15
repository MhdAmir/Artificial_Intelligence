# Using a Python dictionary to act as an adjacency list
graph = {
  '0' : ['3','4'],
  '1' : ['6', "0"],
  '2' : ['5', '6'],
  '3' : ['7', '1'],
  '4' : ['6'],
  '5' : ['7', '6'],
  '6' : ['4', '2'],
  '7' : ['5'],
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
dfs(visited, graph, '0')