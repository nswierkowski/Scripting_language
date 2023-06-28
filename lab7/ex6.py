import logging
import time
import functools

def log(level): 
    def decorator(function):

        def wrapper(args):
            start_time = time.perf_counter()
            result = function(args)
            end_time = time.perf_counter()
            logging.log(level, f"{function.__name__} called with arguments: {args}. Returned {result}. Took {end_time - start_time} seconds.")
            return result       
        
        return wrapper
    
    return decorator

@log(logging.CRITICAL)
def fib(n):
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fib(n-1) + fib(n-2)

if __name__=='__main__':
    print(fib(8))