import unittest
from src.analyzer import Analyzer
from src.modules.text_module import TextModule


analyzer = Analyzer("Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness.")
text_module = TextModule(analyzer)

class TestTextModule(unittest.TestCase):

    def test_get_character_count(self):
        assert text_module.get_character_count() == 111

    def test_get_word_count(self):
        assert text_module.get_word_count() == 21

    def test_get_character_per_word(self):
        assert text_module.get_character_per_word() == 5.29
    
    def test_get_syllable_count(self):
        assert text_module.get_syllable_count() == 41

    def test_get_syllable_count_per_word(self):
        assert text_module.get_syllable_count_per_word() == 1.95

    def test_get_sentence_count(self):
        assert text_module.get_sentence_count() == 1

    def test_get_word_count_per_sentence(self):
        assert text_module.get_word_count_per_sentence() == 21

    def test_get_paragraphs(self):
        assert text_module.get_paragraphs() == [{'id': 1, 'content': 'Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness.'}]

    def test_get_paragraph_count(self):
        assert text_module.get_paragraph_count() == 1

    def test_get_word_count_per_paragraph(self):
        assert text_module.get_word_count_per_paragraph() == 21

    def test_get_sentence_count_per_paragraph(self):
        assert text_module.get_sentence_count_per_paragraph() == 1

    def test_get_unique_word_count(self):
        assert text_module.get_unique_word_count() == 17

    def test_analyze(self):
        assert text_module.analyze() == {
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
    
    def test_name(self):
        assert text_module.name == "text_module"

if __name__ == "__main__":
    unittest.main()