#!/usr/local/bin/python3

import sys
import graphviz
from graph import Graph
from bfs import BFSearch


class Dot:
    def toPNG(self, Graph, path):
        g = graphviz.Graph()
        g.engine = 'neato'
        g.attr('node', label='', color='black', shape='circle', style='filled', width='0.1')
        g.attr('edge', color='grey', penwidth='0.75')

        for v in range(Graph.V):
            g.node(str(v))

        pset = set()
        if len(path) >= 2:
            for i in range(len(path) - 1):
                pset.add((path[i], path[i+1]))
                pset.add((path[i+1], path[i]))

        seen = set()
        for v, e in enumerate(Graph.G):
            for w in e:
                if not (w, v) in seen:
                    if (w,v) in pset:
                        g.edge(str(v), str(w), color='black', penwidth='2.5')
                    else:
                        g.edge(str(v), str(w))
                    seen.add((v,w))


        g.view()


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else ''
    G = Graph(infile)
    print(G.to_string())
    D = Dot()
    B = BFSearch(G, 0)
    D.toPNG(G, B.path_to(249))
