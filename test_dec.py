from functools import wraps

def say_use_decor(func: object) -> object:
    @wraps(func)
    def say(*args,**kwargs) -> None:
        print("Use decorator")
        func(*args,**kwargs)
    
    return say

@say_use_decor
def say_word():
    print("word")

say_word()


