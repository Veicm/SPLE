__all__ = ["two_bodies_repel_each_other"]


def two_bodies_repel_each_other(v1: float, m1: float, m2: float) -> float:
    """
    Calculate the resulting velocity of a second object after two bodies repel each other.

    The calculation is based on the conservation of momentum. It assumes that
    the total momentum before and after the interaction is zero, meaning the
    first object moves with velocity v1 and the second object gains the
    corresponding opposite momentum.

    Example:
        v1 = 2.0, m1 = 1.0, m2 = 1.0
        -> returns -2.0

        v1 = 3.0, m1 = 2.0, m2 = 4.0
        -> returns -1.5

    Args:
        v1 (float):
            Velocity of object 1 in meters per second (m/s).

        m1 (float):
            Mass of object 1 in kilograms (kg).

        m2 (float):
            Mass of object 2 in kilograms (kg).

    Returns:
        float:
            Velocity of object 2 in meters per second (m/s).

    Notes:
        The result follows directly from the conservation of momentum:

        m1 * v1 + m2 * v2 = 0"""
    v2: float = (-(v1 * m1)) / m2
    return v2
