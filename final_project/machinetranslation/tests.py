import unittest

from translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase):
    def test_french_to_english(self):
     self.assertEqual(french_to_english('Oui'), 'Yes')
     self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
     #self.assertNotEqual(french_to_english(''), 'None')
     self.assertNotEqual(french_to_english('Je taime'), 'I hate you')

    def test_english_to_french(self):
     self.assertEqual(english_to_french('Yes'), 'Oui')
     #self.assertNotEqual(english_to_french('None'), '')
     self.assertNotEqual(english_to_french(0), 0)
     self.assertEqual(english_to_french('Hello'), 'Bonjour')

unittest.main()