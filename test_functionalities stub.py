import unittest
import mock
from functionalities import solve_2deg_pol_in_r, NotRealRootError


def solve_2deg_pol_in_c(a: float, b: float, c: float):
    return (1j, 0)


class TestFunctionalitiesFunctions(unittest.TestCase):
    @mock.patch("functionalities.solve_2deg_pol_in_c", solve_2deg_pol_in_c)
    def test_solve_2deg_pol_in_r_stubed_2deg_pol_in_c_with_square_function_raises_error(
        self,
    ) -> None:
        a, b, c = 1, 0, 0
        with self.assertRaises(NotRealRootError):
            solve_2deg_pol_in_r(a, b, c)


if __name__ == "__main__":
    unittest.main()
