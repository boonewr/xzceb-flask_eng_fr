import unittest
import machinetranslation.translator as translator

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(translator.englishToFrench("Hello"), "Bonjour")

        self.assertNotEqual(translator.englishToFrench("Hello"), "Hello")

    def test_frenchToEnglish(self):
        self.assertEqual(translator.frenchToEnglish("Bonjour"), "Hello")

        self.assertNotEqual(translator.frenchToEnglish("Bonjour"), "Bonjour")

if __name__ == '__main__':
    unittest.main()