from .. import gen_or_fn
import unittest
from unittest.mock import Mock, patch

class RunGenOrFn(unittest.TestCase):
    """ Test cases of RunGenOrFn """
        
    def test_fn(self):
        """ Test that a normal function is run properly """
        fn = Mock()
        args = range(3)
        kwargs = {'one': 1, 'two': 2, 'three': 3}
        
        generator = gen_or_fn.RunGenOrFn(fn, *args, **kwargs)
        self.assertRaises(StopIteration, next, generator)
        fn.assert_called_once_with(*args, **kwargs)
        
    def test_generatorFn(self):
        """ Test that a generator function is run properly """
        fn = Mock()
        args = range(3)
        kwargs = {'one': 1, 'two': 2, 'three': 3}
        responses = ['a', 'b', 'c']
        
        generator = gen_or_fn.RunGenOrFn(self.dummy_generator, *args, **kwargs)
        
        try:
            i = 0
            yieldedValue = next(generator)
            self.assertEqual(args[i], yieldedValue)
            while True:
                yieldedValue = generator.send(responses[i])
                i += 1
                self.assertEqual(args[i], yieldedValue)
        except StopIteration:
            pass
            
        self.assertEqual(self.args, tuple(args))
        self.assertEqual(self.kwargs, kwargs)
        self.assertEqual(responses, self.responses)
        
    def dummy_generator(self, *args, **kwargs):
        """ Helper class that acts as a dummy generator """
        self.args = args
        self.kwargs = kwargs
        self.responses = []
        for value in args:
            response = yield value
            self.responses.append(response)

class GenOrFn(unittest.TestCase):
    """ Test cases of GenOrFn """
        
    @patch('kao_generator.gen_or_fn.KaoGenerator')
    def test_generatorBuilt(self, KaoGeneratorMock):
        """ Test that the generator is built properly """
        expected = Mock()
        KaoGeneratorMock.return_value = expected
        fn = Mock()
        args = range(3)
        kwargs = {'one': 1, 'two': 2, 'three': 3}
        
        actual = gen_or_fn.GenOrFn(fn, *args, **kwargs)
        KaoGeneratorMock.assert_called_once_with(gen_or_fn.RunGenOrFn, fn, *args, **kwargs)
        self.assertEqual(actual, expected)