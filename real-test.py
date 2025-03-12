import heapq
import math

# Implementation of a shortest path search (Dijkstra) algorithm
# The idea is to browse a directed graph with the intersections as vertices
# Each edge is weighted with 1 and connects either :
#   - Intersection i, intersection i + 1 and i - 1, in the normal case (if exists)
#   - Intersection i and intersection a_i, in the case of a shortcut

line = input()
count = int(line)

line = input()
shortcuts = list(map(int, line.split(" ")))


def make_edges(n):
    if n == count:
        return [n - 1]

    if n == 1:
        return [n + 1, shortcuts[n - 1]]

    return [n + 1, n - 1, shortcuts[n - 1]]


# Build the graph
edges = {n: make_edges(n) for n in range(1, count + 1)}
costs = count * [math.inf]

# Dijkstra algorithm
costs[0] = 0
queue = [(0, 1)]
while queue:
    cost, u = heapq.heappop(queue)
    if cost != costs[u - 1]:
        continue

    for v in edges[u]:
        alt = costs[u - 1] + 1
        if alt >= costs[v - 1]:
            continue

        costs[v - 1] = alt
        heapq.heappush(queue, (alt, v))


print(" ".join(map(str, costs)))
