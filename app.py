import streamlit as st
from algorithm import prim
from utils import draw_graph, draw_graph_step_by_step

st.set_page_config(page_title="Prim's Algorithm Visualization", layout="wide")

st.title("🌳 Prim's Algorithm - Minimum Spanning Tree")

st.markdown("""
This application demonstrates how Prim's Algorithm constructs a Minimum Spanning Tree (MST) step by step.
Choose a starting node from the sidebar and click the button to run the algorithm.
""")

default_graph = {
    "A": [("B", 3), ("C", 1)],
    "B": [("A", 3), ("D", 4)],
    "C": [("A", 1), ("D", 2)],
    "D": [("B", 4), ("C", 2)]
}

st.sidebar.header("Graph Settings")
start_node = st.sidebar.text_input("Start Node", value="C")

run_button = st.sidebar.button("Run Prim's Algorithm")

if run_button:
    st.subheader("🔍 MST Steps")
    mst, total = prim(default_graph, start_node)

    for u, v, w in mst:
        st.write(f"📍 {u} -- {v} → weight: {w}")

    st.success(f"Total Cost: {total}")

    st.subheader("📊 Visualized Graph")
    mode = st.radio("Visualization Mode", ["Show all", "Step-by-step"])

    if mode == "Step-by-step":
        draw_graph_step_by_step(mst)
    else:
        draw_graph(mst)
