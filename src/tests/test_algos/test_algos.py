from unittest import TestCase


class AlgorithmTest(TestCase):
    def test_fibonacci_algo(self):
        from tasks.algorithms import fibonacci_algo
        self.assertEquals(fibonacci_algo(0), 0)
        self.assertEquals(fibonacci_algo(1), 1)
        self.assertEquals(fibonacci_algo(2), 1)
        self.assertEquals(fibonacci_algo(3), 2)
        self.assertEquals(fibonacci_algo(4), 3)
        self.assertEquals(fibonacci_algo(5), 5)
        self.assertEquals(fibonacci_algo(6), 8)
        self.assertEquals(fibonacci_algo(7), 13)

        self.assertRaises(ValueError, fibonacci_algo, -1)
        self.assertRaises(ValueError, fibonacci_algo, 'N/A')

    def test_factorial_algo(self):
        from tasks.algorithms import factorial_algo
        self.assertEquals(factorial_algo(0), 1)
        self.assertEquals(factorial_algo(1), 1)
        self.assertEquals(factorial_algo(2), 2)
        self.assertEquals(factorial_algo(3), 6)
        self.assertEquals(factorial_algo(4), 24)
        self.assertEquals(factorial_algo(5), 120)

        self.assertRaises(ValueError, factorial_algo, -1)
        self.assertRaises(ValueError, factorial_algo, 'N/A')

    def test_ackermann_algo(self):
        from tasks.algorithms import ackermann_algo
        self.assertEquals(ackermann_algo(0, 0), 1)
        self.assertEquals(ackermann_algo(0, 1), 2)
        self.assertEquals(ackermann_algo(1, 0), 2)
        self.assertEquals(ackermann_algo(1, 1), 3)
        self.assertEquals(ackermann_algo(2, 2), 7)

        self.assertRaises(ValueError, ackermann_algo, -1, 0)
        self.assertRaises(ValueError, ackermann_algo, 0, -1)
        self.assertRaises(ValueError, ackermann_algo, 'N/A', 1)
        self.assertRaises(ValueError, ackermann_algo, 0, 'N/A')
