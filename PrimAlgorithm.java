import java.util.*;

public class PrimAlgorithm {

    public static List<Edge> calculatePrim(Graph graph, Node startNode) {
        List<Edge> mst = new ArrayList<>();
        Set<Node> visited = new HashSet<>();
        PriorityQueue<Edge> pq = new PriorityQueue<>(Comparator.comparingDouble(e -> e.weight));

        visited.add(startNode);
        pq.addAll(graph.getEdgesFrom(startNode));

        while (!pq.isEmpty()) {
            Edge edge = pq.poll();

            if (visited.contains(edge.to)) {
                continue;
            }

            visited.add(edge.to);
            mst.add(edge);

            for (Edge nextEdge : graph.getEdgesFrom(edge.to)) {
                if (!visited.contains(nextEdge.to)) {
                    pq.add(nextEdge);
                }
            }
        }

        return mst;
    }
}
