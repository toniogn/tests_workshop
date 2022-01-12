import unittest
from functionalities import solve_2deg_pol_in_r, solve_2deg_pol_in_c, NotRealRootError


class TestFunctionalitiesFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.a, self.b, self.c = 1, 0, 1

    def test_solve_2deg_pol_in_c_with_square_function_return_zero(self) -> None:
        self.assertEqual(solve_2deg_pol_in_c(self.a, self.b, 0), (0, 0))

    def test_solve_2deg_pol_in_c_with_square_function_equal_negunit_return_junits(
        self,
    ) -> None:
        roots = solve_2deg_pol_in_c(self.a, self.b, self.c)
        self.assertAlmostEqual(roots[0], 1j, places=14)
        self.assertAlmostEqual(roots[1], -1j, places=14)

    def test_solve_2deg_pol_in_r_with_square_function_equal_negunit_raises_error(
        self,
    ) -> None:
        with self.assertRaises(NotRealRootError):
            solve_2deg_pol_in_r(self.a, self.b, self.c)

    def tearDown(self) -> None:
        print(f"Test {self._testMethodName} done !")


if __name__ == "__main__":
    unittest.main()
