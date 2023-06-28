import logging
import time
import functools

def log(level): 
    def decorator(cls):

        def wrapper(*args, **kwargs):
            instance = cls(*args,**kwargs)
            logging.log(level,f"{cls.__name__} instantiated with {args} and {kwargs}")
            return instance
        
        return wrapper
    
    return decorator


@log(logging.CRITICAL)
class this_class:
    def __init__(self, string) -> None:
         self.string = string

if __name__=='__main__':
    new_obj = this_class("Hmm I think this is a class")