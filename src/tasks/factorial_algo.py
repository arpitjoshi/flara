class Factorial(object):

    def __init__(self):
        self._results = 1

    def __compute(self, n: int):
        for i in range(2, n+1):
            self._results = self._results * i

    def sequence(self, n: int) -> int:
        self.__compute(n)
        return self._results

