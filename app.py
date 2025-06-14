import streamlit as st
from algorithm import prim
from utils import draw_graph, draw_graph_step_by_step

st.set_page_config(page_title="Prim's Algorithm Visualization", layout="wide")

st.title("🌳 Prim's Algorithm - Minimum Spanning Tree")

st.markdown("""
Bu uygulama, Prim's Algorithm'in nasıl çalıştığını adım adım gösterir.  
Soldan grafı tanımlayabilir, ardından sonucu görebilirsiniz.
""")

default_graph = {
    "A": [("B", 3), ("C", 1)],
    "B": [("A", 3), ("D", 4)],
    "C": [("A", 1), ("D", 2)],
    "D": [("B", 4), ("C", 2)]
}

st.sidebar.header("Graf Ayarları")
start_node = st.sidebar.text_input("Başlangıç Düğümü", value="C")

run_button = st.sidebar.button("Algoritmayı Çalıştır")

if run_button:
    st.subheader("🔎 MST Adımları")
    mst, total = prim(default_graph, start_node)

    for u, v, w in mst:
        st.write(f"📍 {u} -- {v} → ağırlık: {w}")

    st.success(f"Toplam Maliyet: {total}")

    st.subheader("📊 Görselleştirilmiş Grafik")

    mode = st.radio("Görselleştirme Modu", ["Hepsini göster", "Adım adım göster"])

    if mode == "Adım adım göster":
        draw_graph_step_by_step(mst)
    else:
        draw_graph(mst)

