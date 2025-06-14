# utils.py

import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st

def draw_graph(mst):
    G = nx.Graph()
    
    for u, v, w in mst:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=42)  
    edge_labels = nx.get_edge_attributes(G, 'weight')

    fig, ax = plt.subplots(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_color="#90ee90", node_size=1000, font_size=16, ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

    st.pyplot(fig)

import time
import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st

def draw_graph_step_by_step(mst):
    G = nx.Graph()
    pos = {}
    fig, ax = plt.subplots(figsize=(6, 4))


    all_nodes = set()
    for u, v, _ in mst:
        all_nodes.add(u)
        all_nodes.add(v)
    G.add_nodes_from(all_nodes)
    pos = nx.spring_layout(G, seed=42)

    for i, (u, v, w) in enumerate(mst, 1):
        G.add_edge(u, v, weight=w)

        edge_labels = nx.get_edge_attributes(G, 'weight')

        ax.clear()
        nx.draw(G, pos, with_labels=True, node_color="#add8e6", node_size=1000, font_size=16, ax=ax)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

        st.subheader(f"🔁 Adım {i}: {u} -- {v} (ağırlık: {w})")
        st.pyplot(fig)
        time.sleep(1.2)  

