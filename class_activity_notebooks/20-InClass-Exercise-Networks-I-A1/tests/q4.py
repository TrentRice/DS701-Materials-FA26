from otter.test_files import test_case

OK_FORMAT = False

name = "q4"
points = 0

@test_case(points=None, hidden=False)
def test_clustering_shape(C_real, T_real, p_real, C_rand, clustering_ratio, c_top, n_nodes, n_edges):
    assert 0 <= C_real <= 1 and 0 <= T_real <= 1 and (0 <= C_rand <= 1) and (0 <= c_top <= 1)
    assert abs(p_real - n_edges / (n_nodes * (n_nodes - 1) / 2)) < 1e-12
    assert clustering_ratio > 3, 'a real social network should be several times more clustered than G(n,p)'
    assert abs(clustering_ratio - C_real / C_rand) < 1e-09

