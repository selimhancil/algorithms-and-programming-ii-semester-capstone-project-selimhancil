# 🌲 Prim's Algorithm MST Visualizer

[![Streamlit Cloud](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-cloud-link)

## 🚀 Live Demo
https://algorithms-and-programming-ii-semester-capstone-project-selimh.streamlit.app/
---

## 📖 Project Purpose
This project is an interactive web application to visualize **Prim's Algorithm** for finding the Minimum Spanning Tree (MST) of a weighted undirected graph. Built with Python and Streamlit, it allows users to:
- Create and edit graphs interactively
- Watch step-by-step or animated construction of the MST
- See real-time edge selection and MST cost updates

## 🌟 What is Prim's Algorithm?
Prim's Algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. It starts from an arbitrary node and grows the MST by always choosing the minimum-weight edge that connects a visited node to an unvisited node.

**Applications:** Network design, circuit design, clustering, etc.

---

## 🖼️ Screenshots

| Graph Creation | Step-by-Step Visualization |
|---------------|--------------------------|
| <img width="1680" alt="Ekran Resmi 2025-06-23 22 51 50" src="https://github.com/user-attachments/assets/5f67fb20-17ef-461f-8b30-b9c7b7a2649b" /> | 
<img width="1680" alt="Ekran Resmi 2025-06-23 22 52 53" src="https://github.com/user-attachments/assets/aca64751-cbce-4555-a81b-c4c24d5e1037" /> |


---

## ⏱️ Complexity
- **Time Complexity:** O(E log V) using a min-heap (priority queue)
- **Space Complexity:** O(V + E) for storing the graph and heap

Where V = number of vertices, E = number of edges.

---

## 🧱 Project Structure
```
.
├── app.py              # Main Streamlit app
├── algorithm.py        # Prim's algorithm implementation
├── utils.py            # Helper functions
├── test_algorithm.py   # Unit tests
├── requirements.txt    # Dependencies
├── README.md           # This file
└── data/               # (Optional) Sample graphs
```

---

## 🛠️ How to Run Locally
1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/prims-alg-visualizer.git
   cd prims-alg-visualizer
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```bash
   streamlit run app.py
   ```
4. **Run tests:**
   ```bash
   pytest test_algorithm.py
   ```

---

## ☁️ Deploy on Streamlit Cloud
1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your repo and deploy!

---

## 📚 References
- [CLRS: Introduction to Algorithms](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)
- [Visualgo: MST](https://visualgo.net/en/mst)
- [NetworkX Documentation](https://networkx.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

## 👨‍💻 Author
Selim Han ÇİL (https://github.com/selimhancil)
