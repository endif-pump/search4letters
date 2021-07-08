from functools import wraps
from flask import session

def check_logged_in(func:object) -> object:
    @wraps(func)
    def wrapper(*args,**kwargs):
        if('auth' in session):
            return func(*args,**kwargs)
        else:
            return "You are not logged in"
    
    return wrapper