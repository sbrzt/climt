import pytest
from src.analyzer import Analyzer
from src.modules.text_module import TextModule


sample_text = "Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness."

analyzer = Analyzer(sample_text)
text_module = TextModule(analyzer)


def test_get_character_count():
    assert text_module.get_character_count() == 111

def test_get_word_count():
    assert text_module.get_word_count() == 21

def test_get_character_per_word():
    assert text_module.get_character_per_word() == 5.29

def test_get_sentence_count():
    assert text_module.get_sentence_count() == 1

def test_get_word_count_per_sentence():
    assert text_module.get_word_count_per_sentence() == 21

def test_get_paragraphs():
    assert text_module.get_paragraphs() == [sample_text]

def test_get_paragraph_count():
    assert text_module.get_paragraph_count() == 1

def test_get_word_count_per_paragraph():
    assert text_module.get_word_count_per_paragraph() == 21

def test_get_sentence_count_per_paragraph():
    assert text_module.get_sentence_count_per_paragraph() == 1

def test_get_unique_word_count():
    assert text_module.get_unique_word_count() == 17

def test_analyze():
    assert text_module.analyze() == {
        'character_count': 111, 
        'character_per_word': 5.29, 
        'word_count': 21, 
        'paragraph_count': 1, 
        'words_per_paragraph': 21.0, 
        'sentences_per_paragraph': 1.0, 
        'sentence_count': 1, 
        'words_per_sentence': 21.0, 
        'unique_word_count': 17
    }

def test_name():
    assert text_module.name == "text_analysis"

if __name__ == "__main__":
    unittest.main()