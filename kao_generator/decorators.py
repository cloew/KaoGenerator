from .kao_generator import KaoGenerator

def kao_generator(fn):
    """ Decorator to wrap a generator function in a KaoGenerator class """
    def wrapped(*args, **kwargs):
        """ Return the generator """
        return KaoGenerator(fn, *args, **kwargs)
    return wrapped