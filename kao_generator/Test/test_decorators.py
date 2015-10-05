from .. import decorators
from ..kao_generator import KaoGenerator
import unittest
from unittest.mock import Mock, MagicMock, patch

class kao_generator(unittest.TestCase):
    """ Test cases of kao_generator """
        
    @patch('kao_generator.decorators.KaoGenerator')
    def test_wrapped(self, KaoGeneratorMock):
        """ Test that the function is wrapped in a KaoGenerator """
        expected = "Dummy Generator..."
        args = range(3)
        kwargs = {'one': 1, 'two': 2, 'three': 3}
        KaoGeneratorMock.return_value = expected
        
        decorated = decorators.kao_generator(self.simpleGeneratorFn)
        
        actual = decorated(*args, **kwargs)
        KaoGeneratorMock.assert_called_once_with(self.simpleGeneratorFn, *args, **kwargs)
        self.assertEqual(expected, actual)
    
    def simpleGeneratorFn(self, *args, **kwargs):
            yield 1

class wrap_generators(unittest.TestCase):
    """ Test cases of wrap_generators """
        
    def test_wrapped(self):
        """ Test that the generators are wrapped """
        generators = [MagicMock() for i in range(3)]
        
        for yieldedValue in decorators.wrap_generators(generators):
            pass
            
        for generator in generators:
            generator.__iter__.assert_called_once()
        
    @patch('kao_generator.decorators.KaoGenerator')
    def test_KaoGenerator(self, KaoGeneratorMock):
        """ Test that the generator is returned """
        expected = "Dummy generator..."
        KaoGeneratorMock.return_value = expected
        generators = [MagicMock() for i in range(3)]
        
        actual = decorators.wrap_generators(generators)
        self.assertEqual(expected, actual)