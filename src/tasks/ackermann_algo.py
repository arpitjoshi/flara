class Ackermann(object):

    def __init__(self):
        self._results = None

    def __compute(self, m: int, n: int, s: str = "% s"):
        # print(s % ("A   (% d, % d)" % (m, n)))
        if m == 0:
            return n + 1
        if n == 0:
            return self.__compute(m - 1, 1, s)
        n2 = self.__compute(m, n - 1, s % ("A(% d, %% s)" % (m - 1)))
        return self.__compute(m - 1, n2, s)

    def sequence(self, m: int, n: int) -> int:
        self._results = self.__compute(m, n)
        return self._results
