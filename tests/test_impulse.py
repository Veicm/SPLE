from sple.idealized import impulse as sple_impulse


def test_repel_of_two_bodies():
    v2: float = sple_impulse.two_bodies_repel_each_other(v1=3, m1=2, m2=4)
    assert v2 == -1.5
