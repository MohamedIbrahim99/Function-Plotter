import unittest
import numpy as np
from Main import Function_Plotter as function_plotter

class Test(unittest.TestCase):

    # test case for fixing power sign function
    def test_case0_0 (self):
        result = function_plotter.fix_power_sign(self, "3*x^2 + 1*x+ 4")
        self.assertEqual(result, "3*x**2 + 1*x+ 4")

    # test case for fixing power sign function
    def test_case0_1 (self):
        result = function_plotter.fix_power_sign(self, "5*x^3 + 2*x")
        self.assertEqual(result, "5*x**3 + 2*x")
    
    # test case for fixing power sign function
    def test_case0_2 (self):
        result = function_plotter.fix_power_sign(self, "9*x^3 + 4x^2 + 3*x+6")
        self.assertEqual(result, "9*x**3 + 4x**2 + 3*x+6")

    # test case for fixing power sign function
    def test_case0_3 (self):
        result = function_plotter.fix_power_sign(self, "9 * x ^ 3 + 4 x ^ 2 + 3 * x + 6")
        self.assertEqual(result, "9 * x ** 3 + 4 x ** 2 + 3 * x + 6")

    # -------------------------------------- #

    # test case for is_number function
    def test_case1_0 (self):
        result = function_plotter.is_number(self, "dfg")
        self.assertEqual(result, False)

    # test case for is_number function
    def test_case1_1 (self):
        result = function_plotter.is_number(self, "number")
        self.assertEqual(result, False)

    # test case for is_number function
    def test_case1_2 (self):
        result = function_plotter.is_number(self, "-10")
        self.assertEqual(result, True)

    # test case for is_number function
    def test_case1_3 (self):
        result = function_plotter.is_number(self, "0")
        self.assertEqual(result, True)

    # test case for is_number function
    def test_case1_4 (self):
        result = function_plotter.is_number(self, "200")
        self.assertEqual(result, True)

    # -------------------------------------- #

    # test case to Check if the function input is correct and Calculate y = f(x)
    def test_case2_0 (self):
        x = np.arange(-10, 10.1, 0.1)
        func = "3*x**2 + 1*x+ 4"
        result = function_plotter.f(self, func, x)
        self.assertTrue(np.array_equal(result, eval(func), equal_nan=True))

    # test case to Check if the function input is correct and Calculate y = f(x)
    def test_case2_1 (self):
        x = np.arange(-10, 10.1, 0.1)
        func = "3*x***2 + 1*x+ 4"
        with self.assertRaises(SyntaxError):
            function_plotter.f(self, func, x)

    # test case to Check if the function input is correct and Calculate y = f(x)
    def test_case2_2 (self):
        x = np.arange(-10, 10.1, 0.1)
        func = "3*x**2 + 1*/x+ 4"
        with self.assertRaises(SyntaxError):
            function_plotter.f(self, func, x)

    # test case to Check if the function input is correct and Calculate y = f(x)
    def test_case2_3 (self):
        x = np.arange(-10, 10.1, 0.1)
        func = "3*x**2 + 1*x+ 4/0"
        with self.assertRaises(ZeroDivisionError):
            function_plotter.f(self, func, x)

    # test case to Check if the function input is correct and Calculate y = f(x)
    def test_case2_4 (self):
        x = np.arange(-10, 10.1, 0.1)
        func = "3*x*/2 + 1*x+ 4"
        with self.assertRaises(SyntaxError):
            function_plotter.f(self, func, x)

    # test case to Check if the function input is correct and Calculate y = f(x)
    def test_case2_5 (self):
        x = np.arange(-10, 10.1, 0.1)
        func = "3x**2 + 1*x+ 4"
        with self.assertRaises(SyntaxError):
            function_plotter.f(self, func, x)

    # test case to Check if the function input is correct and Calculate y = f(x)
    def test_case2_6 (self):
        x = np.arange(-10, 10.1, 0.1)
        func = "3*x**2 +"
        with self.assertRaises(SyntaxError):
            function_plotter.f(self, func, x)

    # test case to Check if the function input is correct and Calculate y = f(x)
    def test_case2_7 (self):
        x = np.arange(-10, 10.1, 0.1)
        func = "3*x**2 + 1*y+ 4"
        with self.assertRaises(NameError):
            function_plotter.f(self, func, x)

    # test case to Check if the function input is correct and Calculate y = f(x)
    def test_case2_8 (self):
        x = np.arange(-10, 10.1, 0.1)
        func = "gvhfgh"
        with self.assertRaises(NameError):
            function_plotter.f(self, func, x)

    # -------------------------------------- #

    # test case to Check if the input Min value isn't bigger than Max value 
    def test_case3_0 (self):
        result = function_plotter.check(self, 5, 6)
        self.assertEqual(result, True)

    # test case to Check if the input Min value isn't bigger than Max value 
    def test_case3_1 (self):
        result = function_plotter.check(self, 6, 5)
        self.assertEqual(result, False)

    # test case to Check if the input Min value isn't bigger than Max value 
    def test_case3_2 (self):
        result = function_plotter.check(self, -10, 0)
        self.assertEqual(result, True)

    # test case to Check if the input Min value isn't bigger than Max value 
    def test_case3_3 (self):
        result = function_plotter.check(self, 0, -10)
        self.assertEqual(result, False)


if __name__ == '__main__':  
    unittest.main()  