from typing import Tuple


class NotRealRootError(ValueError):
    ...


def solve_2deg_pol_in_c(a: float, b: float, c: float) -> Tuple[complex, complex]:
    delta = b ** 2 - 4 * a * c
    return (-b + delta ** 0.5) / (2 * a), (-b - delta ** 0.5) / (2 * a)


def solve_2deg_pol_in_r(a: float, b: float, c: float) -> Tuple[float, float]:
    roots = solve_2deg_pol_in_c(a, b, c)
    if any([isinstance(root, complex) for root in roots]):
        raise NotRealRootError
    else:
        return roots
