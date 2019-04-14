'''This problem was asked by Jane Street.

Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.'''

from math import log

def maximum_arbitrage(table):
    log_table = [[-log(edge) for edge in row] for row in table]

    # Pick any source vertex -- we can run Bellman-Ford from any vertex and
    # get the right result
    source = 0
    n = len(log_table)
    min_dist = [float('inf')] * n

    # start currency
    min_dist[0] = 0

    # Relax edges |V - 1| times
    for i in range(n - 1):
        for v in range(n):
            for w in range(n):
                if min_dist[w] > min_dist[v] + log_table[v][w]:
                    print("assigning: min_dist[w] {} min_dist[v] {}".format(min_dist[w], min_dist[v]))
                    min_dist[w] = min_dist[v] + log_table[v][w]

    # If we can still relax edges, then we have a negative cycle
    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + log_table[v][w]:
                return True

    return False


em = [[1, 2, 3], [1./2, 1, 3./2], [1./3, 2./3, 1]]

print("first test:")
print(maximum_arbitrage(em))

em[0][2] = 2.98

print("second test:")
print(maximum_arbitrage(em))
