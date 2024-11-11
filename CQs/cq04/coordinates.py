"cq04"
__author__ = "730767392"


def get_coords(xs: str, ys: str) -> None:
    idx: int = 0
    idx2: int = 0
    xs = xs
    ys = ys
    while idx < len(xs):
        while idx2 < len(ys):
            print(xs[idx] + ys[idx2])
            idx2 = idx2 + 1
        idx = idx + 1
        idx2 = 0
