from .. import decorators
import unittest
from unittest.mock import Mock, patch

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