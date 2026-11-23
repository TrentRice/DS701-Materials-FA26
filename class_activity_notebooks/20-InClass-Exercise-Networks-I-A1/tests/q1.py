from otter.test_files import test_case

OK_FORMAT = False

name = "q1"
points = 0

@test_case(points=None, hidden=False)
def test_graph_and_adjacency(G, A, nodes, edge_list, n_nodes, n_edges, avg_degree, deg_from_A, deg_from_G, degrees_match):
    import numpy as np, networkx as nx
    assert isinstance(G, nx.Graph) and (not G.is_directed()), 'G must be an undirected nx.Graph'
    assert n_nodes == len(nodes) and G.number_of_nodes() == n_nodes
    assert n_edges == len(edge_list) and G.number_of_edges() == n_edges, 'one edge per triple in edge_list'
    assert abs(avg_degree - 2 * n_edges / n_nodes) < 1e-09, 'average degree is 2e/n'
    A = np.asarray(A)
    assert A.shape == (n_nodes, n_nodes), 'A must be n x n'
    assert np.array_equal(A, A.T), 'an undirected graph has a symmetric adjacency matrix'
    assert set(np.unique(A)) <= {0.0, 1.0} and np.all(np.diag(A) == 0), 'unweighted: entries 0/1, no self-loops'
    assert abs(A.sum() / 2 - n_edges) < 1e-09, 'A has each edge twice, so A.sum() = 2e'
    assert np.array_equal(np.asarray(deg_from_A), np.asarray(deg_from_G)) and degrees_match is True

