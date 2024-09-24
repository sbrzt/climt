import unittest
from src.analyzer import Analyzer
from src.modules.text_module import TextModule


analyzer = Analyzer("Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness.")

class TestAnalyzer(unittest.TestCase):

    def test_get_text(self):
        assert analyzer.get_text() == "Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness."

    def test_get_words(self):
        assert analyzer.get_words() == ["Blessed", "is", "he", "who", "in", "the", "name", "of", "charity", "and", "good", "will", "shepherds", "the", "weak", "through", "the", "valley", "of", "the", "darkness"]

    def test_get_sentences(self):
        assert analyzer.get_sentences() == [{"id": 1, "content": "Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness."}]

    def test_get_preprocessed_text(self):
        assert analyzer.get_preprocessed_text() == "blessed name charity good shepherd weak valley darkness"

    def test_get_preprocessed_words(self):
        assert analyzer.get_preprocessed_words() == ["blessed", "name", "charity", "good", "shepherd", "weak", "valley", "darkness"]

if __name__ == "__main__":
    unittest.main()