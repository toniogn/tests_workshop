import unittest
from functionalities import solve_2deg_pol_in_r, solve_2deg_pol_in_c, NotRealRootError


class TestFunctionalitiesFunctions(unittest.TestCase):
    def test_solve_2deg_pol_in_c_with_square_function_return_zero(self) -> None:
        a, b, c = 1, 0, 0
        self.assertEqual(solve_2deg_pol_in_c(a, b, c), (0, 0))

    def test_solve_2deg_pol_in_c_with_square_function_equal_negunit_return_junits(self) -> None:
        a, b, c = 1, 0, 1
        roots = solve_2deg_pol_in_c(a, b, c)
        self.assertAlmostEqual(roots[0], 1j, places=14)
        self.assertAlmostEqual(roots[1], -1j, places=14)

    def test_solve_2deg_pol_in_r_with_square_function_equal_negunit_raises_error(self) -> None:
        a, b, c = 1, 0, 1
        with self.assertRaises(NotRealRootError):
            solve_2deg_pol_in_r(a, b, c)


if __name__ == "__main__":
    unittest.main()
