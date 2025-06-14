# algorithm.py

import heapq

def prim(graph, start_node):
    visited = set()
    mst = []
    total_weight = 0
    min_heap = [(0, start_node, None)]  

    while min_heap:
        weight, current, prev = heapq.heappop(min_heap)

        if current in visited:
            continue

        visited.add(current)

        if prev is not None:
            mst.append((prev, current, weight))
            total_weight += weight

        for neighbor, edge_weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return mst, total_weight


# Test kısmı
if __name__ == "__main__":
    graph = {
        "A": [("B", 3), ("C", 1)],
        "B": [("A", 3), ("D", 4)],
        "C": [("A", 1), ("D", 2)],
        "D": [("B", 4), ("C", 2)]
    }

    mst, total = prim(graph, "C")
    print("Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"{u} -- {v} == {w}")
    print(f"Toplam Maliyet: {total}")

