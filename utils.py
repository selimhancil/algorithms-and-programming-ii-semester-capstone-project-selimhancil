"""
utils.py
Helper functions for graph generation, formatting, and conversion.
"""
from typing import Dict, List, Tuple
import random

def generate_random_graph(num_nodes: int, edge_prob: float = 0.4, min_weight: int = 1, max_weight: int = 10) -> Dict[int, List[Tuple[int, float]]]:
    """
    Generate a random undirected weighted graph as an adjacency list.
    Args:
        num_nodes: Number of nodes in the graph
        edge_prob: Probability of edge creation between any two nodes
        min_weight: Minimum edge weight
        max_weight: Maximum edge weight
    Returns:
        Adjacency list representation of the graph
    """
    graph = {i: [] for i in range(num_nodes)}
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            if random.random() < edge_prob:
                weight = random.randint(min_weight, max_weight)
                graph[i].append((j, weight))
                graph[j].append((i, weight))
    return graph

def graph_to_edge_list(graph: Dict[int, List[Tuple[int, float]]]) -> List[Tuple[int, int, float]]:
    """
    Convert adjacency list to edge list (no duplicates for undirected graph).
    """
    edges = set()
    for u in graph:
        for v, w in graph[u]:
            if (v, u) not in edges:
                edges.add((u, v))
    return [(u, v, w) for u, v in edges for _, w in graph[u] if v == _]

def edge_list_to_graph(edge_list: List[Tuple[int, int, float]], num_nodes: int) -> Dict[int, List[Tuple[int, float]]]:
    """
    Convert edge list to adjacency list.
    """
    graph = {i: [] for i in range(num_nodes)}
    for u, v, w in edge_list:
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph

def format_graph_for_display(graph: Dict[int, List[Tuple[int, float]]]) -> str:
    """
    Format the graph as a string for display.
    """
    lines = []
    for u in graph:
        for v, w in graph[u]:
            if u < v:
                lines.append(f"{u} --({w})-- {v}")
    return "\n".join(lines) 