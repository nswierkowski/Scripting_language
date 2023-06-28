from ex4 import make_generator
from ex4 import fib
from functools import lru_cache

@lru_cache(maxsize=None)
def make_generator_mem(function):

    def memoized(n):
        return function(n)

    return make_generator(memoized)
    
if __name__=='__main__':
    gen = make_generator_mem(fib)
    number_of_iter = 10
    for _ in range(number_of_iter):
        print(next(gen))

    print("-----------------------------------------")

    gen = make_generator_mem(lambda x : 2**x)
    number_of_iter = 10
    for _ in range(number_of_iter):
        print(next(gen))