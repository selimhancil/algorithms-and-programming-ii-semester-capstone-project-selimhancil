"""
algorithm.py
Implementation of Prim's Algorithm for Minimum Spanning Tree (MST) with visualization hooks.
"""
from typing import Dict, List, Tuple, Callable, Optional, Set
import heapq

class Edge:
    def __init__(self, u: int, v: int, weight: float):
        self.u = u
        self.v = v
        self.weight = weight
    def __repr__(self):
        return f"Edge({self.u}, {self.v}, {self.weight})"

Graph = Dict[int, List[Tuple[int, float]]]


def prim_mst(
    graph: Graph,
    start: int = 0,
    on_step: Optional[Callable[[Set[int], List[Edge], List[Edge], float], None]] = None
) -> Tuple[List[Edge], float]:
    """
    Prim's Algorithm for Minimum Spanning Tree (MST).
    Args:
        graph: Adjacency list representation {node: [(neighbor, weight), ...]}
        start: Starting node for Prim's algorithm
        on_step: Optional callback called at each step with:
            - visited: set of visited nodes
            - mst_edges: list of edges in the MST so far
            - candidate_edges: list of candidate edges in the priority queue
            - current_cost: current total cost of the MST
    Returns:
        mst_edges: List of edges in the MST
        total_cost: Total weight of the MST
    """
    visited = set([start])
    edges = []
    mst_edges = []
    total_cost = 0.0

    for v, w in graph.get(start, []):
        heapq.heappush(edges, (w, start, v))

    while edges and len(visited) < len(graph):
        w, u, v = heapq.heappop(edges)
        if v in visited:
            continue
        visited.add(v)
        mst_edges.append(Edge(u, v, w))
        total_cost += w
        for to, weight in graph.get(v, []):
            if to not in visited:
                heapq.heappush(edges, (weight, v, to))
        if on_step:
            # Prepare candidate edges for visualization
            candidate_edges = [Edge(u1, v1, w1) for (w1, u1, v1) in edges]
            on_step(set(visited), list(mst_edges), candidate_edges, total_cost)
    if on_step:
        on_step(set(visited), list(mst_edges), [], total_cost)
    return mst_edges, total_cost 