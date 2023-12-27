
def create_martirx(num_nodes):
    # Initialize an empty adjacency matrix
    graph = [[float('inf')] * num_nodes for _ in range(num_nodes)]

    # For each node, set the distance to itself as 0
    for i in range(num_nodes):
        graph[i][i] = 0

    return graph

num_nodes = 8 


connectivity_matrix = create_martirx(num_nodes)
values = [
#   [0,1,2,3,4,5,6,7]
    [0,1,0,0,0,0,0,0],#0
    [1,1,1,1,0,0,0,0],#1
    [0,1,1,0,1,0,0,0],#2
    [0,1,0,1,0,0,1,0],#3
    [0,0,1,0,1,0,0,11],#4
    [0,0,0,0,0,1,1,1],#5
    [0,0,0,1,0,1,1,22],#6
    [0,0,0,0,1,1,1,1],#7
]
for i in range(num_nodes):
    for j in range(num_nodes):
        if i == j:
            connectivity_matrix[i][j] = 0
        elif values[i][j] == 0:
            connectivity_matrix[i][j] =float('inf')
        else:
            connectivity_matrix[i][j] = values[i][j] 
     
def algo(graph, start):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    distance = [float('inf')] * num_nodes
    distance[start] = 0

    for i in range(num_nodes):
        min_distance = float('inf')
        index = -1
        for j in range(num_nodes):
            if not visited[j] and distance[j] < min_distance:#selecting the first non visit
                index = j  ; # but as this is a loop, last indexed min distance will be selected
                min_distance =  distance[j] 

        if index == -1:
            break ;  # if no index found then break 

        visited[index] = True

        # now loop for the selected index
        for i in range(num_nodes):
            if not visited[i] and graph[index][i]!= float('inf'):
                new_distance = distance[index] + graph[index] [i]


            if not visited[i] and graph[index][i] != float('inf'):
                new_distance = distance[index] + graph[index][i]
                if new_distance < distance[i]:
                    distance[i] = new_distance
                    if new_distance < distance[i]:
                        distance[i] = new_distance
    return distance ;





num_nodes = 4  # Change this to the number of nodes in your graph
adjacency_matrix = [
    [0, 2, 4, 1],  # Example adjacency matrix, adjust according to your graph
    [2, 0, 1, 5],
    [4, 1, 0, 6],
    [1, 5, 6, 0]
]

start_node = 0  # Start from node 0
shortest_distances = algo(connectivity_matrix, start_node)
print("Shortest distances from node {} to all other nodes: {}".format(start_node, shortest_distances))

#now as  i want the shortest path as node 

k = len(connectivity_matrix)
end_node = 7 
#print(k)
index = end_node

print(end_node)
for _ in range(k):

    
   

    for i in range(k):
        #print(i)
        if ( shortest_distances[index] - connectivity_matrix[i][index]) == shortest_distances[i]:
            
            index = i
            print(index)
            
            
            


