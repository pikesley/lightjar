from lib.gamma_correct import gamma_correct


def test_gamma_correction():
    """Test gamma correction."""
    assert gamma_correct([255, 0, 0]) == [255, 0, 0]
    assert gamma_correct([0, 0, 0]) == [0, 0, 0]
    assert gamma_correct([127, 5, 240]) == [36, 0, 215]
