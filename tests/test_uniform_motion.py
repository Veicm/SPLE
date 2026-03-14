from sple.idealized import uniform_motion


def test_uniformly_rapid_motion_s():
    result: float = uniform_motion.uniformly_rapid_motion_s(t=3, v=4, s0=2)
    assert result == 14


def test_uniformly_accelerated_motion_s():
    result: float = uniform_motion.uniformly_accelerated_motion_s(t=3, a=1, v0=2, s0=0)
    assert result == 10.5


def test_uniformly_accelerated_motion_v():
    result: float = uniform_motion.uniformly_accelerated_motion_v(a=1, t=5, v0=2)
    assert result == 7
