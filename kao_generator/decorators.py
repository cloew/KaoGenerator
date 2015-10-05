from .kao_generator import KaoGenerator

def kao_generator(fn):
    """ Decorator to wrap a generator function in a KaoGenerator class """
    def wrapped(*args, **kwargs):
        """ Return the generator """
        return KaoGenerator(fn, *args, **kwargs)
    return wrapped
    
def wrap_generators(generators):
    """ Return a Kao Generator that wraps several other KaoGenerators """
    def run():
        """ Run the generators """
        for generator in generators:
            for request in generator:
                response = yield request
                generator.queue(response)
    return KaoGenerator(run)