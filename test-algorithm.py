import unittest
from algorithm import prim

class TestPrimAlgorithm(unittest.TestCase):

    def test_basic_graph(self):
        graph = {
            "A": [("B", 1), ("C", 2)],
            "B": [("A", 1), ("C", 3)],
            "C": [("A", 2), ("B", 3)]
        }
        mst, total = prim(graph, "A")
        self.assertEqual(len(mst), 2)
        self.assertEqual(total, 3)

    def test_single_node(self):
        graph = {
            "A": []
        }
        mst, total = prim(graph, "A")
        self.assertEqual(mst, [])
        self.assertEqual(total, 0)

    def test_disconnected_graph(self):
        graph = {
            "A": [("B", 1)],
            "B": [("A", 1)],
            "C": []
        }
        mst, total = prim(graph, "A")
        self.assertTrue(("C" not in [v for _, v, _ in mst]))
        self.assertLessEqual(len(mst), 1)

if __name__ == "__main__":
    unittest.main()

