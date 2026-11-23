from otter.test_files import test_case

OK_FORMAT = False

name = "q3"
points = 0

@test_case(points=None, hidden=False)
def test_ccdf_and_shapes(ccdf, p_match, ER2, BA, N_BA, deg_ba, deg_er, max_deg_ba, max_deg_er, frac_hubs_ba, frac_hubs_er):
    import numpy as np
    x, p = ccdf(np.array([1, 1, 2, 3]))
    assert list(x) == [1, 2, 3] and np.allclose(p, [1.0, 0.5, 0.25]), 'ccdf: unique x, fraction with degree >= x'
    assert abs(p_match - BA.number_of_edges() / (N_BA * (N_BA - 1) / 2)) < 1e-12, 'p = e / C(n, 2)'
    assert ER2.number_of_nodes() == N_BA
    assert len(deg_ba) == len(deg_er) == N_BA
    assert max_deg_ba == max(deg_ba) and max_deg_er == max(deg_er)
    assert 0 <= frac_hubs_er <= frac_hubs_ba <= 1, 'the BA graph should have MORE hubs than G(n,p)'
    assert max_deg_ba > 2 * max_deg_er, 'the heavy tail should give a far larger max degree'

