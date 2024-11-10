import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        minimum_v = 1
        maximum_v = 10
        for _ in range(1600):  # Test a large number of random values
            random_num = function_A(minimum_v, maximum_v)
            self.assertTrue(minimum_v <= random_num <= maximum_v)

    def test_function_B(self):
        # TODO
        result = function_B()
        self.assertIn(result, ['+', '-', '*'])
        pass

    def test_function_C(self):
        test_cases = [
            (15, 5, '+', '8 + 2', 7),
            (23, 11, '-', "13 - 2", 9),
            (14, 9, '*', "8 * 5", 25)
        ]

        for no1, no2, operator, predicted_problem, predicted_answer in test_cases:
                question, answer = function_C(no1, no2, operator)
                self.assertEqual(question, predicted_problem)
                self.assertEqual(answer, predicted_answer)
                pass

if __name__ == "__main__":
    unittest.main()
