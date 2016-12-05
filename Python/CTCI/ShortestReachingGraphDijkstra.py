# Contains Bellman-Ford algorithm.
import sys
import collections
import heapq


class Graph(object):
    def __init__(self, size):
        self.vertexes = [0] * size
        self.edges = collections.defaultdict(set)
        self.size = size

    def find_all_distances(self, start_node_index):
        distance = [sys.maxint] * self.size
        predecessor = [-1] * self.size

        distance[start_node_index] = 0
        unvisited_nodes = zip(distance, range(len(distance)))
        heapq.heapify(unvisited_nodes)
        unv_nodes_set = set(range(self.size))

        # Relax edges repeatedly.
        while len(unvisited_nodes):
            cost, origin = heapq.heappop(unvisited_nodes)
            unv_nodes_set.remove(origin)

            possible_targets = (self.edges[origin] & unv_nodes_set)

            for dst in possible_targets:
                # Two checks as *undirected* graph, otherwise only one check required.
                if distance[origin] + 6 < distance[dst]:
                    original_dist = distance[dst]
                    distance[dst] = distance[origin] + 6
                    predecessor[dst] = origin

                    # Update heap.
                    replacement_ind = unvisited_nodes.index((original_dist, dst))
                    unvisited_nodes[replacement_ind] = (distance[dst], dst)
                    heapq.heapify(unvisited_nodes)

        del distance[start_node_index]
        # Print distances.
        output = " ".join([str(x) if x < sys.maxint else str(-1) for x in distance])
        print output
        return distance

    def connect(self, source, dest):
        self.edges[source].add(dest)
        self.edges[dest].add(source)


t = input()
for i in range(t):
    n, m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x, y = [int(x) for x in raw_input().split()]
        graph.connect(x - 1, y - 1)
    s = input()
    graph.find_all_distances(s - 1)
