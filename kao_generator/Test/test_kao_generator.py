from ..kao_generator import KaoGenerator
import unittest
from unittest.mock import Mock

class init(unittest.TestCase):
    """ Test cases of initialization """
        
    def test_GeneratorBuilt(self):
        """ Test that the generator is built properly """
        generator = Mock()
        genFn = Mock(return_value=generator)
        args = range(3)
        kwargs = {'one': 1, 'two': 2, 'three': 3}
        
        wrapper = KaoGenerator(genFn, *args, **kwargs)
        genFn.assert_called_once_with(*args, **kwargs)
        self.assertEqual(wrapper.generator, generator)
        
    def test_EmptyQueue(self):
        """ Test that the queue is empty after initialization """
        genFn = Mock(return_value=None)
        
        wrapper = KaoGenerator(genFn)
        self.assertEqual(len(wrapper._queue), 0)