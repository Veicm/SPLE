__all__ = [
    "uniformly_rapid_motion_s",
    "uniformly_accelerated_motion_s",
    "uniformly_accelerated_motion_v",
]


def uniformly_rapid_motion_s(t: float, v: float, s0: float = 0) -> float:
    """
    Calculate the position of an object moving with constant velocity.

    The motion follows the equation of uniformly rapid motion, where the
    velocity remains constant over time.

    Example:
        t = 5, v = 2, s0 = 0
        -> returns 10

        t = 3, v = 4, s0 = 2
        -> returns 14

    Args:
        t (float):
            Time passed in seconds (s).

        v (float):
            Constant velocity in meters per second (m/s).

        s0 (float):
            Initial position in meters (m). Defaults to 0.

    Returns:
        float:
            Position of the object in meters (m).

    Notes:
        The position is calculated using the equation:

        s = v * t + s0
    """
    s: float = v * t + s0
    return s


def uniformly_accelerated_motion_s(
    t: float, a: float, v0: float = 0, s0: float = 0
) -> float:
    """
    Calculate the position of an object undergoing uniform acceleration.

    The function computes the displacement of an object when the acceleration
    remains constant over time.

    Example:
        t = 2, a = 2, v0 = 0, s0 = 0
        -> returns 4

        t = 3, a = 1, v0 = 2, s0 = 0
        -> returns 10.5

    Args:
        t (float):
            Time passed in seconds (s).

        a (float):
            Constant acceleration in meters per second squared (m/s²).

        v0 (float):
            Initial velocity in meters per second (m/s). Defaults to 0.

        s0 (float):
            Initial position in meters (m). Defaults to 0.

    Returns:
        float:
            Position of the object in meters (m).

    Notes:
        The displacement is calculated using the equation:

        s = 1/2 * a * t^2 + v0 * t + s0
    """
    s: float = (1 / 2) * a * (t**2) + v0 * t + s0
    return s


def uniformly_accelerated_motion_v(a: float, t: float, v0: float = 0) -> float:
    """
    Calculate the velocity of an object under constant acceleration.

    The function determines the velocity after a given time when the
    acceleration remains constant.

    Example:
        a = 2, t = 3, v0 = 0
        -> returns 6

        a = 1, t = 5, v0 = 2
        -> returns 7

    Args:
        a (float):
            Constant acceleration in meters per second squared (m/s²).

        t (float):
            Time passed in seconds (s).

        v0 (float):
            Initial velocity in meters per second (m/s). Defaults to 0.

    Returns:
        float:
            Velocity of the object in meters per second (m/s).

    Notes:
        The velocity is calculated using the equation:

        v = a * t + v0
    """
    v: float = a * t + v0
    return v
