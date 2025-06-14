import heapq

def prim(graph, start):
    visited = set()
    mst = []
    total_weight = 0
    edges = [(0, start, start)]

    while edges:
        weight, u, v = heapq.heappop(edges)
        if v in visited:
            continue
        visited.add(v)
        if u != v:
            mst.append((u, v, weight))
            total_weight += weight
        for neighbor, w in graph.get(v, []):
            if neighbor not in visited:
                heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight
