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

class iter(unittest.TestCase):
    """ Test cases of iter """
        
    def test_queueUsed(self):
        """ Test that the the queue values are popped and sent to the generator """
        items = [1,2,3,4,5]
        queueValues = ['a', 'b', 'c', 'd', 'e']
        
        generator = Mock()
        generator.send = Mock(side_effect=items)
        genFn = Mock(return_value=generator)
        
        wrapper = KaoGenerator(genFn)
        for v in queueValues:
            wrapper.queue(v)
            
        for i, yieldedValue in enumerate(wrapper):
            self.assertEqual(items[i], yieldedValue)
            generator.send.assert_called_with(queueValues[i])

class queue(unittest.TestCase):
    """ Test cases of queue """
        
    def test_appended(self):
        """ Test that the value is appended to the queue """
        genFn = Mock(return_value=None)
        expected = 123
        
        wrapper = KaoGenerator(genFn)
        wrapper.queue(expected)
        actual = wrapper._queue.popleft()
        self.assertEqual(expected, actual)

class pop(unittest.TestCase):
    """ Test cases of pop """
        
    def test_valueInQueue(self):
        """ Test that the value from the queue is retrieved """
        genFn = Mock(return_value=None)
        expected = 123
        
        wrapper = KaoGenerator(genFn)
        wrapper.queue(expected)
        actual = wrapper.pop()
        self.assertEqual(expected, actual)
        
    def test_noValueInQueue(self):
        """ Test that None is returned when the queue is empty """
        genFn = Mock(return_value=None)
        expected = None
        
        wrapper = KaoGenerator(genFn)
        self.assertEqual(len(wrapper._queue), 0)
        actual = wrapper.pop()
        self.assertEqual(expected, actual)