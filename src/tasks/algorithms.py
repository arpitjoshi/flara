from tasks.fibonacci_algo import Fibonacci
from tasks.factorial_algo import Factorial
from tasks.ackermann_algo import Ackermann
from tasks import timeit


@timeit
def fibonacci_algo(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("Not an Integer")
    if n < 0:
        raise ValueError("Negative Integer")

    fib = Fibonacci().sequence(n)
    return fib


@timeit
def factorial_algo(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("Not an Integer")
    if n < 0:
        raise ValueError("Negative Integer")

    fac = Factorial().sequence(n)
    return fac


@timeit
def ackermann_algo(m: int, n: int, s="% s") -> int:
    if not isinstance(n, int):
        raise ValueError("Not an Integer")
    if not isinstance(m, int):
        raise ValueError("Not an Integer")
    if (n < 0) or (m < 0):
        raise ValueError("Negative Integer")

    ack = Ackermann().sequence(m, n)
    return ack
