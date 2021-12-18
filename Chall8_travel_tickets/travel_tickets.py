#!/usr/bin/env python3

from collections import defaultdict
import sys


# Tarjan's algorithm for finding articulation points
# https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/
# This class represents an undirected graph
# using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
        self.Time = 0


    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    '''A recursive function that fin articulation points
    using DFS traversal
    u --> The vertex to be visited next
    visited[] --> Keeps track of visited vertices
    disc[] --> Stores discovery times of visited vertives
    parent[] --> Stores parent vertives in DFS tree
    ap[] --> Store articulation points'''
    def APUtil(self, u, visited, ap, parent, low, disc):
        # Count the children in current node
        children = 0

        # Mark the current node as visited
        visited[u] = True

        # Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        # Recur for all the vertives adjacent to this vertex
        for v in self.graph[u]:
            # If v is not visited yet, then make it a child of u
            # in DFS tree and recur for it
            if visited[v] == False:
                parent[v] = u
                children += 1
                self.APUtil(v, visited, ap, parent, low, disc)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                low[u] = min(low[u], low[v])

                # u is an articulation point in followint cases
                # (1) u is root of DFS tree and has two or more children.
                if parent[u] == -1 and children > 1:
                    ap[u] = True

                # (2) If u is not root and low value of one of its child is more
                # than discovery value of u.
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True

            # Update low value of u for parent function calls
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])


    # The function to do DFS traversal. It uses recursive APUtil()
    def AP(self):

        # Mark all the vertices as not visited,
        # and initialize parent and visited,
        # and ap(articulation points) arrays
        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)
        ap = [False] * (self.V) # To store articulation points

        # Call the recursive helper function
        # to find articulation points
        # in DFS tree rooted with vertex 'i'
        for i in range(self.V):
            if visited[i] == False:
                self.APUtil(i, visited, ap, parent, low, disc)

        return [index for index, value in enumerate(ap) if value == True]


def critical_cities():
    tickets = int(sys.stdin.readline().rstrip())
    edges_city = []
    edges_index = []
    city_to_index = {}
    index_to_city = {}

    index = 0
    for _ in range(tickets):
        cityA, cityB = sys.stdin.readline().rstrip().split(",")
        if cityA not in city_to_index:
            city_to_index[cityA] = index
            index_to_city[index] = cityA
            index += 1
        if cityB not in city_to_index:
            city_to_index[cityB] = index
            index_to_city[index] = cityB
            index += 1
        edges_city.append([cityA, cityB])
        edges_index.append([city_to_index[cityA], city_to_index[cityB]])
    
    graph = Graph(len(city_to_index))
    for edge in edges_index:
        graph.addEdge(edge[0], edge[1])
    ap_indexes = graph.AP()
    ap_cities = sorted([index_to_city[i] for i in ap_indexes])
    return ",".join(ap_cities) if len(ap_cities) else "-"


def main():
    cases = int(sys.stdin.readline().rstrip())
    for i in range(cases):
        print("Case #{}: {}".format(str(i + 1), critical_cities()))
    return 0


if __name__ == '__main__':
    sys.exit(main())
