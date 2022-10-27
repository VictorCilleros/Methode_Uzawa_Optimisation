import unittest
import numpy as np
from functions import calcul_f


class TestMarkov(unittest.TestCase):
    def test_matrix_f(self):
        x1,x2 = 2,2
        self.assertEqual(calcul_f(x1,x2).shape,(2,))
        self.assertEqual(calcul_f(x1,x2)[0],7)
        self.assertEqual(calcul_f(x1,x2)[1],3)

