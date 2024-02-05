print("""
import sys
MAX_value=999

def bellman_ford(number_of_vertices,source,adjacency_matrix):
    distances=[MAX_value]*(number_of_vertices+1)
    distances[source]=0
    
    for _ in range(number_of_vertices-1):
        for source_node in range(1,number_of_vertices+1):
            for destination_node in range(1,number_of_vertices+1):
                if adjacency_matrix[source_node][destination_node] != MAX_value:
                    new_distance= distances[source_node]+adjacency_matrix[source_node][destination_node]
                    if distances[destination_node]>new_distance:
                        distances[destination_node]=new_distance
    for vertex in range(1,number_of_vertices+1):
        print("distance of source ",source,"to",vertex,"is",distances[vertex])
        
number_of_vertices= int(input("Enter the number of Vertices:"))
adjacency_matrix=[[MAX_value]*(number_of_vertices+1)for _ in range(number_of_vertices+1)]

print("ENTER THE ADJACENCY MATRIX:")
for source_node in range(1,number_of_vertices+1):
    for destination_node in range(1,number_of_vertices+1):
        adjacency_matrix[source_node][destination_node]=int(input())
        if source_node == destination_node:
            adjacency_matrix[source_node][destination_node]=0
        elif adjacency_matrix[source_node][destination_node]==0:
            adjacency_matrix[source_node][destination_node]=MAX_value
        
source=int(input("Enter the source Vertex:"))
bellman_ford(number_of_vertices,source,adjacency_matrix)        



output --- 
Enter the number of Vertices:4
ENTER THE ADJACENCY MATRIX:
0
5
0
0
5
0
3
4
0
3
0
2
0
4
2
0
Enter the source Vertex:2
distance of source  2 to 1 is 5
distance of source  2 to 2 is 0
distance of source  2 to 3 is 3
distance of source  2 to 4 is 4""")