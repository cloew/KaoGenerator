from kao_decorators import proxy_for

from collections import deque
import inspect

@proxy_for('generator', ['send', '__next__'])
class KaoGenerator:
    """ Helper class to facilitate dealing with generators """
    
    def __init__(self, generatorFn, *args, **kwargs):
        """ Initialize with the generator """
        self.generator = generatorFn(*args, **kwargs)
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