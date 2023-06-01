import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def test_englishToFrench2(self):
        self.assertNotEqual(englishToFrench("Hello"), "Hello")

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

    def test_frenchToEnglish2(self):
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Bonjour")

if __name__ == '__main__':
    unittest.main()