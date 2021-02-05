def check_access(func):

    def wrapper(obj, *args, **kwargs):
        if obj.has_access():
            return func(obj, *args, **kwargs)
        else:
            raise Exception("access denied!")

    return wrapper
