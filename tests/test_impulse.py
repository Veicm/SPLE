from sple_physics import idealized as sple_ideal


def test_repel_of_two_bodies():
    v2: float = sple_ideal.impulse.two_bodies_repel_each_other(v1=3, m1=2, m2=4)
    assert v2 == -1.5
