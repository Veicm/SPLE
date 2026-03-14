__all__ = ["completely_inelastic_collision", "completely_elastic_collision"]


def completely_inelastic_collision(m1: float, v1: float, m2: float, v2: float) -> float:
    """
    Calculate the final velocity of two bodies after a completely inelastic collision.

    In a completely inelastic collision the two objects stick together after the
    collision and move with a common velocity. The resulting velocity is determined
    using the conservation of momentum.

    Example:
        m1 = 2, v1 = 4
        m2 = 2, v2 = 0
        -> returns 2

        m1 = 1, v1 = 3
        m2 = 3, v2 = 1
        -> returns 1.5

    Args:
        m1 (float):
            Mass of object 1 in kilograms (kg).

        v1 (float):
            Velocity of object 1 before the collision in meters per second (m/s).

        m2 (float):
            Mass of object 2 in kilograms (kg).

        v2 (float):
            Velocity of object 2 before the collision in meters per second (m/s).

    Returns:
        float:
            The shared velocity of both objects after the collision in meters
            per second (m/s).

    Notes:
        The velocity is calculated using the conservation of momentum:

        m1 * v1 + m2 * v2 = (m1 + m2) * u
    """
    u = ((m1 * v1) + (m2 * v2)) / (m1 + m2)
    return u


def completely_elastic_collision(
    m_r: float, v_r: float, m_g: float, v_g: float
) -> float:
    """
    Calculate the resulting velocity of one object after a completely elastic collision.

    A completely elastic collision conserves both momentum and kinetic energy.
    This function returns the post-collision velocity of the object whose
    properties are marked with the suffix `_r`.

    Example:
        m_r = 1, v_r = 3
        m_g = 1, v_g = 0
        -> returns 0

        m_r = 2, v_r = 4
        m_g = 1, v_g = 0
        -> returns 1.33

    Args:
        m_r (float):
            Mass of the object whose resulting velocity should be calculated
            (return object) in kilograms (kg).

        v_r (float):
            Initial velocity of the return object in meters per second (m/s).

        m_g (float):
            Mass of the other object involved in the collision (given object)
            in kilograms (kg).

        v_g (float):
            Initial velocity of the other object in meters per second (m/s).

    Returns:
        float:
            Velocity of the return object after the collision in meters per
            second (m/s).

    Notes:
        `_r` denotes the object whose resulting velocity is returned.

        `_g` denotes the other object involved in the collision.

        The velocity is calculated using the one-dimensional elastic collision
        equation.
    """
    u_r = ((m_r - m_g) * v_r + (2 * m_g * v_g)) / (m_r + m_g)
    return u_r
