def bfs(visited,queue,start,dict):
    visited.append(start)
    queue.append(start)
    while queue:
        m=queue.pop(0)
        print(m , end=" ")
        for neighbour in dict[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

dict = {}
n= int(input('number of nodes : '))
for i in range (n):
    node_name = input("enter node name :")
    x = int(input('number of nodes it connected to : '))
    edges = []
    for j in range(x):
        edges.append(input(f"enter the {j+1} node : "))
    dict[node_name]=edges
print(dict)
visited = []
queue = []
start = input("enter start node : ")
bfs(visited,queue,start,dict)
print("")
