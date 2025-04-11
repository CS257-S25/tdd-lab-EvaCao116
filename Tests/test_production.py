'''
A file for tests for the production code.
'''
import unittest
from production import reverse_word

class TestReverseWord(unittest.TestCase):
    def test_reverse_word(self):
        """
        Test that it can reverse the word
        """
        word = "Seven"
        result = reverse_word(word)
        self.assertEqual(result, "neveS")

if __name__ == '__main__':
    unittest.main()