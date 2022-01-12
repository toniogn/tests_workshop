import unittest


class TestClass(unittest.TestCase):
    def test_method_do_something(self) -> None:
        pass


class TestModuleFunctions(unittest.TestCase):
    def test_function_do_something(self) -> None:
        pass


if __name__ == "__main__": #Ces deux lignes servent à lancer les tests lors d'un
    unittest.main()        #appel du script, elles seront omises par la suite
