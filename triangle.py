def area(a, h):
    if a < 0 or h < 0:
        raise ValueError
    return a * h / 2


def perimeter(a):
    if a < 0:
        raise ValueError
    return 3 * a