
def make_generator(function):
    def generator(n=0):
        yield function(n)
        yield from generator(n+1)
    return generator()

# def fib(n):
#     def fib_in(n, act, prev):
#         match n:
#             case 0:
#                 return prev
#             case 1:
#                 return act
#             case _:
#                 return fib_in(n-1, act+prev, act)
#     return fib_in(n, 1, 0)

def fib(n):
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fib(n-1) + fib(n-2)


if __name__=='__main__':
    gen = make_generator(fib)
    number_of_iter = 10
    for _ in range(number_of_iter):
        print(next(gen))

    print("-----------------------------------------")

    gen = make_generator(lambda x : 2**x)
    number_of_iter = 10
    for _ in range(number_of_iter):
        print(next(gen))
