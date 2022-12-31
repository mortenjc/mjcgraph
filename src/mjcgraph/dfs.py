#!/usr/local/bin/python3

import sys
import pydot
from graph import Graph

class DFSearch():
    def __init__(self, G, s):
        self.marked = [False for i in range(G.V)]
        self.edgeTo = [-1 for i in range(G.V)]
        self.s = s
        self.dfs(G, s)


    def dfs(self, Graph, v):
        self.marked[v] = True
        for w in Graph.adj(v):
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(Graph, w)


    def has_path_to(self, v):
        return self.marked[v]


    def path_to(self, v):
        path = []
        if not self.has_path_to(v):
            return path
        x = v
        while x != self.s:
            path.append(x)
            x = self.edgeTo[x]
        return path


    def count(self):
        return sum([1 for x in self.marked if x == True]) - 1


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else ''
    G = Graph(infile)
    print(G.to_string())

    search = DFSearch(G, 0)
    n = search.count()
    print(f'there are {n} vertices connected to {0}')
    print(search.path_to(100))
