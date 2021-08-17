# Lucas Sequence L is a sequence of numbers
# such that L(n) = L(n-1) + L(n-2)

from time import perf_counter
from math import sqrt
from doctest import testmod
import sys


class Stopwatch:
    def __init__(self):
        self.reset()

    def start(self):
        if not self.__running:
            self.__start_time = perf_counter()
            self.__running = True
        else:
            print('Stopwatch already running')

    def stop(self):
        if self.__running:
            self.__elapsed += perf_counter()-self.__start_time
            self.__running = False
        else:
            print('Stopwatch not running')

    def reset(self):
        self.__start_time = self.__elapsed = 0
        self.__running = False

    def elapsed(self):
        if not self.__running:
            return self.__elapsed
        else:
            print('Stopwatch must be stopped')
            return None


def print_time(time:float) -> None:
    print('\nElapsed: ', end="")
    if time > 1.0:
        elapsed = round(time, 3)
        print('%.3f s' % elapsed)
    elif time > 0.001:
        elapsed = time*1000
        elapsed = round(elapsed, 2)
        print('%.2f ms' % elapsed)
    else:
        elapsed = time*1000000
        elapsed = round(elapsed, 2)
        print('%.2f µs' % elapsed)


def lucas_sequence(n0: int, n1: int, n2: int) -> None:
    L0, L1 = n0, n1
    if n2 >= 1:
        print(L0, end=" ")
    if n2 >= 2:
        print(L1, end=" ")
    for i in range(0, n2-2):
        print(L0+L1, end=" ")
        L0, L1 = L1, L0+L1


def lucas_sequence_timer(n0: int, n1: int, n2: int) -> None:
    timer = Stopwatch()
    timer.start()
    L0, L1 = n0, n1
    if n2 >= 1:
        print(L0, end=" ")
    if n2 >= 2:
        print(L1, end=" ")
    for i in range(0, n2-2):
        print(L0+L1, end=" ")
        L0, L1 = L1, L0+L1
    timer.stop()
    print_time(timer.elapsed())


def lucas_sequence_last(n0: int, n1: int, n2: int) -> None:
    L0, L1 = n0, n1
    for i in range(0, n2-2):
        L0, L1 = L1, L0+L1
    print(L1, end=" ")


def lucas_sequence_last_timer(n0: int, n1: int, n2: int) -> None:
    timer = Stopwatch()
    timer.start()
    L0, L1 = n0, n1
    for i in range(0, n2-2):
        L0, L1 = L1, L0+L1
    print(L1, end=" ")
    timer.stop()
    print_time(timer.elapsed())


def test_lucas_sequence():
    """
    >>> lucas_sequence(0,0,6)
    0 0 0 0 0 0 
    >>> lucas_sequence(2,1,10)
    2 1 3 4 7 11 18 29 47 76 
    >>> lucas_sequence(1,1,12)
    1 1 2 3 5 8 13 21 34 55 89 144 
    >>> lucas_sequence(2308,4261,5)
    2308 4261 6569 10830 17399 
    >>> lucas_sequence(5,-20,6)
    5 -20 -15 -35 -50 -85 
    >>> lucas_sequence_last(2,1,100)
    489526700523968661124 
    """
    pass


if __name__ == "__main__":
    if(sys.argv[3:]):
        lucas_sequence(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    else:
        testmod()
