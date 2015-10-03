from collections import deque
import inspect

class KaoGenerator:
    """ Helper class to facilitate dealing with generators """
    
    def __init__(self, generatorFn, *args, **kwargs):
        """ Initialize with the generator """
        if inspect.isgenerator(generatorFn):
            self.generator = generatorFn
        elif inspect.isgeneratorfunction(generatorFn):
            self.generator = generatorFn(*args, **kwargs)
        else:
            raise TypeError('Received non-generator object')
        self._queue = deque()
        
    def __iter__(self):
        """ Return the iterator for this class """
        def iter_wrapper():
            while True:
                yield self.generator.send(self.pop())
        return iter_wrapper()
        
    def queue(self, value):
        """ Queue up the given value """
        self._queue.append(value)
            
    def pop(self):
        """ Pop the enxt element from the queue if there is one otherwise None """
        return self._queue.popleft() if len(self._queue) > 0 else None