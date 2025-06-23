import pytest
from algorithm import prim_mst, Edge

def test_simple_triangle():
    graph = {0: [(1, 1.0), (2, 2.0)], 1: [(0, 1.0), (2, 3.0)], 2: [(0, 2.0), (1, 3.0)]}
    mst, cost = prim_mst(graph, 0)
    assert cost == 3.0
    assert len(mst) == 2
    assert set((e.u, e.v) for e in mst) == {(0, 1), (0, 2)} or set((e.u, e.v) for e in mst) == {(1, 0), (2, 0)}

def test_disconnected_graph():
    graph = {0: [(1, 1.0)], 1: [(0, 1.0)], 2: []}
    mst, cost = prim_mst(graph, 0)
    # Only connects 0 and 1, node 2 is unreachable
    assert len(mst) == 1
    assert cost == 1.0

def test_single_node():
    graph = {0: []}
    mst, cost = prim_mst(graph, 0)
    assert mst == []
    assert cost == 0.0

def test_empty_graph():
    graph = {}
    mst, cost = prim_mst(graph, 0)
    assert mst == []
    assert cost == 0.0

def test_on_step_callback():
    graph = {0: [(1, 1.0)], 1: [(0, 1.0)]}
    steps = []
    def on_step(visited, mst_edges, candidate_edges, cost):
        steps.append((set(visited), list(mst_edges), list(candidate_edges), cost))
    mst, cost = prim_mst(graph, 0, on_step)
    assert len(steps) > 0
    assert steps[-1][1] == mst
    assert steps[-1][3] == cost 