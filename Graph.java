import java.util.*;
import java.util.stream.Collectors;

public class Graph {
    private List<Node> nodes;
    private List<Edge> edges;

    public Graph() {
        this.nodes = new ArrayList<>();
        this.edges = new ArrayList<>();
    }

    public void addNode(Node node) {
        nodes.add(node);
    }

    public void addEdge(Edge edge) {
        edges.add(edge);
    }

    public List<Node> getNodes() {
        return nodes;
    }

    public List<Edge> getEdges() {
        return edges;
    }

    public List<Edge> getEdgesFrom(Node node) {
        return edges.stream()
                .filter(e -> e.from.equals(node))
                .collect(Collectors.toList());
    }
}
