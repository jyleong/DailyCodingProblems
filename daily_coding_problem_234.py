'''
Recall that the minimum spanning tree is the subset of edges of a tree that connect all its vertices with the smallest possible total edge weight. Given an undirected graph with weighted edges, compute the maximum weight spanning tree.
'''

class Edge(object):
    def __init__(self, src, target, weight):
        self.src = src
        self.target = target
        self.weight = weight

    def __repr__(self):
        return "({})--{}-->({})\n".format(self.src, self.weight, self.target)

class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_parent = self.find(parent, x)
        y_parent = self.find(parent, y)

        if rank[x_parent] < rank[y_parent]:
            parent[x_parent] = y_parent
        elif rank[x_parent] > rank[y_parent]:
            parent[y_parent] = x_parent
        else:
            parent[x_parent] = y_parent
            rank[y_parent] += 1

    def kruskal_max(self):
        self.edges = sorted(self.edges, key=lambda e: e.weight, reverse=True)

        parent = []
        rank = []
        for i in range(self.vertices):
            parent.append(i)
            rank.append(0)
        num_e = 0
        cur_e = 0
        result_weight = 0
        result_edges = []
        while num_e < self.vertices-1:

            edge = self.edges[cur_e]
            x = self.find(parent, edge.src)
            y = self.find(parent, edge.target)
            cur_e += 1

            if x != y:
                num_e += 1
                result_weight += edge.weight
                result_edges.append(edge)
                self.union(parent, rank, x, y)
        print("Added edges")
        for e in result_edges:
            print(e)
        print("Total weight: %d" % result_weight)
        return result_weight


if __name__ == '__main__':

    g = Graph(5)
    g.add_edge(Edge(0, 2, 5))
    g.add_edge(Edge(0, 1, 3))
    g.add_edge(Edge(1, 3, 9))
    g.add_edge(Edge(1, 2, 3))
    g.add_edge(Edge(2, 4, 8))
    g.add_edge(Edge(3, 4, 2))
    g.add_edge(Edge(2, 3, 4))

    g.kruskal_max()

