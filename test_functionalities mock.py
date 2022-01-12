import unittest
import mock
from functionalities import solve_2deg_pol_in_r, NotRealRootError


class TestFunctionalitiesFunctions(unittest.TestCase):
    def test_solve_2deg_pol_in_r_mocked_2deg_pol_in_c_with_square_function_raises_error(
        self,
    ) -> None:
        a, b, c = 1, 0, 0
        with mock.patch(
            "functionalities.solve_2deg_pol_in_c", mock.Mock(return_value=(1j, 0))
        ) as mocked_solve_2deg_pol_in_c:
            with self.assertRaises(NotRealRootError):
                solve_2deg_pol_in_r(a, b, c)
                mocked_solve_2deg_pol_in_c.assert_called_once_with(a, b, c)


if __name__ == "__main__":
    unittest.main()
