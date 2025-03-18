from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    '''
    Generates a Fibonacci calculator with caching for improved performance.

    This function returns an internal function `fibonacci(n)` that calculates the 
    nth Fibonacci number using memoization. It stores already calculated Fibonacci 
    numbers in a cache (dictionary) to avoid redundant calculations.

    Returns:
        Callable[[int], int] - A function that takes an integer n as input 
        and returns the nth Fibonacci number.

    Example:
        fib = caching_fibonacci()
        print(fib(10))  # Outputs: 55
    '''
    cache = {} # dictionary for storing the results of calculating Fibonacci numbers

    def fibonacci(n: int) -> int:
        if n<= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        #print(cache)
        return cache[n]

    return fibonacci

if __name__ == "__main__":
    fibnum = caching_fibonacci()

    assert fibnum(-1) == 0
    assert fibnum(0) == 0
    assert fibnum(1) == 1
    assert fibnum(2) == 1
    assert fibnum(3) == 2
    assert fibnum(7) == 13
    assert fibnum(32) == 2178309
    assert fibnum(199) == 173402521172797813159685037284371942044301




