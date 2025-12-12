import unittest

from Coche import Coche


class TestCoche(unittest.TestCase):
    def test_evolucionar_sets_itv_and_levels_once(self):
        coche = Coche("TestCar", "Earth")
        nivel_inicial = coche.nivel

        for _ in range(5):
            coche.evolucionar()

        self.assertEqual(coche.nivel, nivel_inicial + 5)
        self.assertTrue(coche.itv)


if __name__ == "__main__":
    unittest.main()
