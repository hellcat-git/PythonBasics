from functools import reduce


def li(prev_el, el):
    return prev_el + el


print(reduce(li, map(int, [el for el in range(100, 1001, 2)])))
