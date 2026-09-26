def volume(a):
    if a < 0:
        raise ValueError
    return a * a * a

def area(a):
    if a < 0:
        raise ValueError
    return a * a * 6