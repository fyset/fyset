

def wrap(wrapper):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            return wrapper(func, *args, **kwargs)
        return inner_wrapper
    return outer_wrapper
