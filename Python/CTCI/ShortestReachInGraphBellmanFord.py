# Contains Bellman-Ford algorithm.
import sys


class Graph(object):
    def __init__(self, size):
        self.vertexes = [0] * size
        self.edges = []
        self.size = size

    def find_all_distances(self, start_node_index):
        def add_if_not_in_set(q, s, el):
            if el not in s:
                q.append(el)
                s.add(el)
        distance = [sys.maxint] * self.size
        predecessor = [-1] * self.size

        distance[start_node_index] = 0
        candidates = [start_node_index]
        candidate_set = {start_node_index}

        # Relax edges repeatedly.
        while len(candidates):
            u = candidates.pop(0)
            candidate_set.remove(u)

            for edge in self.edges:
                src, dst, weight = edge
                if not (src == u or dst == u):
                    continue
                # Two checks as *undirected* graph, otherwise only one check required.
                if distance[src] + weight < distance[dst]:
                    distance[dst] = distance[src] + weight
                    predecessor[dst] = src
                    add_if_not_in_set(candidates, candidate_set, dst)

        # TODO: detect negative cycles.

        del distance[start_node_index]
        # Print distances.
        output = " ".join([str(x) if x < sys.maxint else str(-1) for x in distance])
        print output
        return distance

    def connect(self, source, dest):
        self.edges.append((source, dest, 6))
        self.edges.append((dest, source, 6))


t = input()
for i in range(t):
    n, m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x, y = [int(x) for x in raw_input().split()]
        graph.connect(x - 1, y - 1)
    s = input()
    graph.find_all_distances(s - 1)
