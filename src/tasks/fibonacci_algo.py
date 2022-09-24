class Fibonacci(object):

    def __init__(self):
        self._results = [0, 1]

    def __compute(self, n: int):
        for i in range(len(self._results), n+1):
            self._results.append(self._results[i - 1] + self._results[i - 2])

    def sequence(self, n: int) -> int:
        self.__compute(n)
        return self._results[n]

