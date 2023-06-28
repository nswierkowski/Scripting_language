import random

class PasswordGenerator:
    """
    Class generate password
    """

    def __init__(self, length, charset, count) -> None:
        self.length = length
        self.charset = list(charset)
        self.count = count

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count == 0:
            raise StopIteration
        self.count -= 1
        return "".join(map(lambda x : random.choice(self.charset), [None]*self.length))
        
if __name__=='__main__':
    number_of_passwords = 5
    pass_gen = PasswordGenerator(5, {'a', 'b', 'c', 'd', 'e'}, number_of_passwords)
    it = iter(pass_gen)
    # print(next(it))
    # print(next(it))
    # print(next(it))
    # print(next(it))
    # print(next(it))
    # print(next(it))

    for _ in range(number_of_passwords):
        print(next(it))