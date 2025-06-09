import matplotlib.pyplot as plt
import networkx as nx
import time

def visualize_prims_algorithm(graph_data):
    G = nx.Graph()

    # Tüm düğümleri ve kenarları grafiğe ekle
    for node in graph_data['nodes']:
        G.add_node(node)

    for edge in graph_data['edges']:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    pos = nx.spring_layout(G, seed=42)  # düğümleri konumlandır

    visited = set()
    mst_edges = []

    current_node = graph_data['nodes'][0]
    visited.add(current_node)

    plt.ion()

    while len(visited) < len(graph_data['nodes']):
        edges = []

        for u in visited:
            for v in G.neighbors(u):
                if v not in visited:
                    weight = G[u][v]['weight']
                    edges.append((u, v, weight))

        if not edges:
            break

        edges.sort(key=lambda x: x[2])
        u, v, weight = edges[0]
        mst_edges.append((u, v))
        visited.add(v)

        # GÖRSELLEŞTİRME
        plt.clf()
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
        nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='r', width=2)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title("Prim's Algorithm - MST Growing")
        plt.pause(1)

    plt.ioff()
    plt.show()


if __name__ == "__main__":
    graph_data = {
        'nodes': ['A', 'B', 'C', 'D', 'E'],
        'edges': [
            ('A', 'B', 2),
            ('A', 'C', 3),
            ('B', 'C', 1),
            ('B', 'D', 4),
            ('C', 'D', 5),
            ('C', 'E', 7),
            ('D', 'E', 6),
        ]
    }

    visualize_prims_algorithm(graph_data)
