# A simple decorator to turn your class into a singleton.
# Making it thread safe  and all that jazz.
from functools import wraps
def singleton(f):
    _instance = None

    @wraps(f)
    def inner(*args, **kwargs):
        nonlocal _instance
        _instance = f(*args, **kwargs) if _instance is None else _instance
        return _instance

    return inner
