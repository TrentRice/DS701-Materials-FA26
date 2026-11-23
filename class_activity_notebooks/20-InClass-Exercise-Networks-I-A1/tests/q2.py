from otter.test_files import test_case

OK_FORMAT = False

name = "q2"
points = 0

@test_case(points=None, hidden=False)
def test_components_shape(components, n_comp_er, n_isolated_er, largest_er, size_largest_er, diam_largest_er, n_comp_real, diam_real, n_within_2, ER, G, N_ER):
    import networkx as nx
    assert n_comp_real == 1 and isinstance(diam_real, int) and (diam_real >= 2)
    assert 0 <= n_within_2 < G.number_of_nodes()
    assert isinstance(components, list) and all((isinstance(c, set) for c in components)), 'components: a list of sets'
    assert sum((len(c) for c in components)) == N_ER, 'components must partition all 200 nodes'
    assert [len(c) for c in components] == sorted((len(c) for c in components), reverse=True), 'sort largest first'
    assert n_comp_er == len(components) and n_isolated_er == sum((1 for c in components if len(c) == 1))
    assert size_largest_er == len(components[0]) == largest_er.number_of_nodes()
    assert nx.is_connected(largest_er) and isinstance(diam_largest_er, int) and (diam_largest_er >= 1)

