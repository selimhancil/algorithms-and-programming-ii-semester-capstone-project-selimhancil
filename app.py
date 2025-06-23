import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import time
from typing import List, Set
from algorithm import prim_mst, Edge
from utils import generate_random_graph, graph_to_edge_list, edge_list_to_graph

st.set_page_config(page_title="Prim's Algorithm Visualizer", layout="wide")
st.title("🌲 Prim's Algorithm MST Visualizer")

# --- Sidebar Controls ---
st.sidebar.header("Graph Controls")
num_nodes = st.sidebar.slider("Number of nodes", 3, 12, 6)
edge_prob = st.sidebar.slider("Edge probability", 0.2, 1.0, 0.5, 0.05)
min_weight = st.sidebar.number_input("Min edge weight", 1, 100, 1)
max_weight = st.sidebar.number_input("Max edge weight", min_weight, 100, 10)

if 'graph' not in st.session_state or st.sidebar.button("Generate Random Graph"):
    st.session_state.graph = generate_random_graph(num_nodes, edge_prob, min_weight, max_weight)
    st.session_state.edge_list = graph_to_edge_list(st.session_state.graph)
    st.session_state.num_nodes = num_nodes

# --- Graph Editing ---
st.sidebar.subheader("Edit Edges")
edge_to_edit = st.sidebar.selectbox(
    "Select edge to edit/remove", [f"{u}-{v} (w={w})" for u, v, w in st.session_state.edge_list] + ["Add new edge"]
)
if edge_to_edit != "Add new edge":
    idx = [f"{u}-{v} (w={w})" for u, v, w in st.session_state.edge_list].index(edge_to_edit)
    u, v, w = st.session_state.edge_list[idx]
    new_weight = st.sidebar.number_input("Edit weight", 1, 100, int(w), key="edit_weight")
    if st.sidebar.button("Update Edge"):
        st.session_state.edge_list[idx] = (u, v, new_weight)
        st.session_state.graph = edge_list_to_graph(st.session_state.edge_list, st.session_state.num_nodes)
    if st.sidebar.button("Remove Edge"):
        st.session_state.edge_list.pop(idx)
        st.session_state.graph = edge_list_to_graph(st.session_state.edge_list, st.session_state.num_nodes)
else:
    u_new = st.sidebar.number_input("Node 1", 0, num_nodes-1, 0, key="add_u")
    v_new = st.sidebar.number_input("Node 2", 0, num_nodes-1, 1, key="add_v")
    w_new = st.sidebar.number_input("Weight", 1, 100, 1, key="add_w")
    if st.sidebar.button("Add Edge") and u_new != v_new:
        st.session_state.edge_list.append((u_new, v_new, w_new))
        st.session_state.graph = edge_list_to_graph(st.session_state.edge_list, st.session_state.num_nodes)

# --- Visualization State ---
if 'prim_steps' not in st.session_state:
    st.session_state.prim_steps = []
    st.session_state.prim_idx = 0
    st.session_state.auto_run = False
    st.session_state.speed = 1.0

def collect_steps(graph, start):
    steps = []
    def on_step(visited: Set[int], mst_edges: List[Edge], candidate_edges: List[Edge], cost: float):
        steps.append((set(visited), list(mst_edges), list(candidate_edges), cost))
    prim_mst(graph, start, on_step)
    return steps

# --- Controls for Prim's Algorithm ---
st.sidebar.header("Prim's Algorithm Controls")
start_node = st.sidebar.number_input("Start node", 0, num_nodes-1, 0)
mode = st.sidebar.radio("Mode", ["Step-by-step", "Auto-run"])
speed = st.sidebar.slider("Animation speed (sec/step)", 0.1, 2.0, 1.0, 0.1)

if st.sidebar.button("Run Prim's Algorithm") or st.session_state.prim_steps == [] or st.session_state.num_nodes != num_nodes:
    st.session_state.prim_steps = collect_steps(st.session_state.graph, start_node)
    st.session_state.prim_idx = 0
    st.session_state.auto_run = (mode == "Auto-run")
    st.session_state.speed = speed

# --- Step/Auto Controls ---
col1, col2 = st.columns([1, 2])
with col1:
    st.subheader("Controls")
    if st.session_state.prim_steps:
        if mode == "Step-by-step":
            if st.button("Next Step"):
                if st.session_state.prim_idx < len(st.session_state.prim_steps) - 1:
                    st.session_state.prim_idx += 1
            if st.button("Previous Step"):
                if st.session_state.prim_idx > 0:
                    st.session_state.prim_idx -= 1
        else:
            if st.session_state.prim_idx < len(st.session_state.prim_steps) - 1:
                time.sleep(st.session_state.speed)
                st.session_state.prim_idx += 1
                st.rerun()
    st.write(f"Step: {st.session_state.prim_idx+1} / {len(st.session_state.prim_steps)}")

# --- Visualization ---
with col2:
    st.subheader("Graph Visualization")
    if st.session_state.prim_steps:
        visited, mst_edges, candidate_edges, cost = st.session_state.prim_steps[st.session_state.prim_idx]
        G = nx.Graph()
        for u in range(num_nodes):
            G.add_node(u)
        for u, v, w in st.session_state.edge_list:
            G.add_edge(u, v, weight=w)
        pos = nx.spring_layout(G, seed=42)
        edge_colors = []
        edge_widths = []
        for u, v in G.edges():
            in_mst = any((e.u == u and e.v == v) or (e.u == v and e.v == u) for e in mst_edges)
            in_cand = any((e.u == u and e.v == v) or (e.u == v and e.v == u) for e in candidate_edges)
            if in_mst:
                edge_colors.append('green')
                edge_widths.append(3)
            elif in_cand:
                edge_colors.append('orange')
                edge_widths.append(2)
            else:
                edge_colors.append('gray')
                edge_widths.append(1)
        node_colors = ['lightgreen' if n in visited else 'lightgray' for n in G.nodes()]
        plt.figure(figsize=(7, 5))
        nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, width=edge_widths, node_size=700)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        st.pyplot(plt.gcf())
        st.markdown(f"**Current MST Cost:** {cost}")
        st.markdown(f"**Visited Nodes:** {sorted(list(visited))}")
        st.markdown(f"**MST Edges:** {[f'({e.u}, {e.v}, w={e.weight})' for e in mst_edges]}")
    else:
        st.info("Run Prim's Algorithm to visualize the MST.")

st.markdown("---")
st.markdown("""
**Legend:**
- <span style='color:green'>Green edges</span>: In MST<br>
- <span style='color:orange'>Orange edges</span>: Candidate edges<br>
- <span style='color:gray'>Gray edges</span>: Not yet considered<br>
- <span style='color:lightgreen'>Light green nodes</span>: Visited<br>
- <span style='color:lightgray'>Gray nodes</span>: Not visited
""", unsafe_allow_html=True)

st.caption("Developed for Prim's Algorithm visualization. [GitHub](#) | [Streamlit Cloud](#)") 