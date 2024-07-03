import unittest
from logic.number_to_words_converter import FrenchNumberToWordsConverter


class TestFrenchNumberToWordsConverter(unittest.TestCase):
    def setUp(self):
        self.converter = FrenchNumberToWordsConverter()

    def test_units(self):
        self.assertEqual(self.converter.transform(0), "zéro")
        self.assertEqual(self.converter.transform(1), "un")
        self.assertEqual(self.converter.transform(16), "seize")

    def test_tens(self):
        self.assertEqual(self.converter.transform(20), "vingt")
        self.assertEqual(self.converter.transform(21), "vingt-et-un")
        self.assertEqual(self.converter.transform(77), "soixante-dix-sept")
        self.assertEqual(self.converter.transform(71), "soixante-et-onze")
        self.assertEqual(self.converter.transform(81), "quatre-vingt-un")
        self.assertEqual(self.converter.transform(91), "quatre-vingt-onze")

    def test_hundreds(self):
        self.assertEqual(self.converter.transform(100), "cent")
        self.assertEqual(self.converter.transform(101), "cent-un")
        self.assertEqual(self.converter.transform(252), "deux-cent-cinquante-deux")
        self.assertEqual(self.converter.transform(200), "deux-cents")

    def test_thousands(self):
        self.assertEqual(self.converter.transform(1000), "mille")
        self.assertEqual(self.converter.transform(1100), "mille-cents")
        self.assertEqual(self.converter.transform(2045), "deux-mille-quarante-cinq")
        self.assertEqual(self.converter.transform(200000), "deux-cent-milles")


if __name__ == "__main__":
    unittest.main()
