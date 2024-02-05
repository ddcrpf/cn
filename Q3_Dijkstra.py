print("""
import sys

total_vertex=9

def minimum_distance(distance,sp_set):
    m=sys.maxsize
    m_index =-1
    for vx in range(total_vertex):
        if sp_set[vx] == False and distance[vx]<= m:
            m=distance[vx]
            m_index = vx
    return m_index
def print_solution(distance,n):
    print("The shortest Distance from source 0th node to all other nodes are :")
    for j in range(n):
        print("to",j,"the shortest distance is ",distance[j])
    
def dijkstra(graph,s):
    distance = [sys.maxsize]*total_vertex
    sp_set=[False]* total_vertex
    distance[s]= 0
    for _ in range(total_vertex-1):
        u = minimum_distance(distance,sp_set)
        sp_set[u]=True
        
        for v in range(total_vertex):
            if sp_set[v]== False and graph[u][v] != -1 and distance[u]!= sys.maxsize and distance[u]+graph[u][v] <distance[v]:
                distance[v]=distance[u]+graph[u][v]
    print_solution(distance,total_vertex)
    
graph=[[-1,3,-1,-1,-1,-1,-1,7,-1],
      [3,-1,7,-1,-1,-1,-1,10,4],
      [-1,7,-1,6,-1,2,-1,-1,1],
      [-1,-1,6,-1,8,13,-1,-1,3],
      [-1,-1,-1,8,-1,9,-1,-1,-1],
      [-1,-1,2,13,9,-1,4,-1,5],
      [-1,-1,-1,-1,-1,4,-1,2,5],
      [7,10,-1,-1,-1,-1,2,-1,6],
      [-1,4,1,3,-1,5,5,6,-1]]
dijkstra(graph,0)




output -- 
The shortest Distance from source 0th node to all other nodes are :
to 0 the shortest distance is  0
to 1 the shortest distance is  3
to 2 the shortest distance is  8
to 3 the shortest distance is  10
to 4 the shortest distance is  18
to 5 the shortest distance is  10
to 6 the shortest distance is  9
to 7 the shortest distance is  7
to 8 the shortest distance is  7""")