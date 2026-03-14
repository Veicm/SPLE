from sple.idealized import straight_joints


def test_completely_inelastic_collision():
    result: float = straight_joints.completely_inelastic_collision(
        m1=1, v1=3, m2=3, v2=1
    )
    assert result == 1.5


def test_completely_elastic_collision():
    result: float = straight_joints.completely_elastic_collision(
        m_r=1, v_r=3, m_g=1, v_g=0
    )
    assert result == 0
