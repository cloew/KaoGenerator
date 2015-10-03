from .kao_generator import KaoGenerator
import inspect

def RunGenOrFn(function, *args, **kwargs):
    """ Runs the given function as a generator or as a standard function """
    if inspect.isgeneratorfunction(function):
        generator = KaoGenerator(function, *args, **kwargs)
        for yieldedValue in generator:
            response = yield yieldedValue
            generator.queue(response)
    else:
        function(*args, **kwargs)
        
def GenOrFn(function, *args, **kwargs):
    """ Helepr function to return a KaoGenerator wrapping the RunGenOrFn """
    return KaoGenerator(RunGenOrFn, function, *args, **kwargs)