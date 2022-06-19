import unittest
from unittest import TestCase

from main import reserveList, bookerineManagement_iterativo, bookerineManagement_recursivo


class Test(TestCase):
    def test_bookerine_management_1_reserves_iterativo(self):

        reserves, solution = reserveList(1)
        idTable =  bookerineManagement_iterativo(reserves)

        self.assertEqual(idTable, solution)

    def test_bookerine_management_2_reserves_iterativo(self):

        reserves, solution = reserveList(2)
        idTable =  bookerineManagement_iterativo(reserves)

        self.assertEqual(idTable, solution)

    def test_bookerine_management_5_reserves_iterativo(self):
        reserves, solution = reserveList(5)
        idTable = bookerineManagement_iterativo(reserves)

        self.assertEqual(idTable, solution)

    def test_bookerine_management_10_reserves_iterativo(self):
        reserves, solution = reserveList(10)
        idTable = bookerineManagement_iterativo(reserves)

        self.assertEqual(idTable, solution)

    def test_bookerine_management_20_reserves_iterativo(self):
        reserves, solution = reserveList(20)
        idTable = bookerineManagement_iterativo(reserves)

        self.assertEqual(idTable, solution)

    def test_final_bookerine_validation_iterativo (self):
        for step in range(10,100,10):
            reserves, solution = reserveList(step)
            idTable = bookerineManagement_iterativo(reserves)
            self.assertEqual(idTable, solution)

    def test_bookerine_management_1_reserves_recursivo(self):

        reserves, solution = reserveList(1)
        idTable =  bookerineManagement_recursivo(reserves)

        self.assertEqual(idTable, solution)

    def test_bookerine_management_2_reserves_recursivo(self):

        reserves, solution = reserveList(2)
        idTable =  bookerineManagement_recursivo(reserves)

        self.assertEqual(idTable, solution)

    def test_bookerine_management_5_reserves_recursivo(self):
        reserves, solution = reserveList(5)
        idTable = bookerineManagement_recursivo(reserves)

        self.assertEqual(idTable, solution)

    def test_bookerine_management_10_reserves_recursivo(self):
        reserves, solution = reserveList(10)
        idTable = bookerineManagement_recursivo(reserves)

        self.assertEqual(idTable, solution)

    def test_bookerine_management_20_reserves_recursivo(self):
        reserves, solution = reserveList(20)
        idTable = bookerineManagement_recursivo(reserves)

        self.assertEqual(idTable, solution)

    def test_final_bookerine_validation_recursivo (self):
        for step in range(10,100,10):
            reserves, solution = reserveList(step)
            idTable = bookerineManagement_recursivo(reserves)
            self.assertEqual(idTable, solution)

if __name__ == '__main__':
    unittest.main()