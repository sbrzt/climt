import unittest
from src.analyzer import Analyzer


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

    def test_generate_analysis(self):
        analyzer.plug_modules("text")
        assert analyzer.generate_analysis() == {
            'text_analysis': 
                {
                    'character_count': 111, 
                    'character_per_word': 5.29, 
                    'syllable_count': 41, 
                    'syllables_per_word': 1.95, 
                    'word_count': 21, 
                    'paragraph_count': 1, 
                    'words_per_paragraph': 21.0, 
                    'sentences_per_paragraph': 1.0, 
                    'sentence_count': 1, 
                    'words_per_sentence': 21.0, 
                    'unique_word_count': 17
                }
            }

if __name__ == "__main__":
    unittest.main()