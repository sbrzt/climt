import pytest
from src.analyzer import Analyzer


sample_text = "Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness."

analyzer = Analyzer(sample_text)


def test_get_text():
    assert analyzer.get_text() == sample_text

def test_get_words():
    assert analyzer.get_words() == [
        "Blessed", "is", "he", "who", "in", "the", "name", "of", 
        "charity", "and", "good", "will", "shepherds", "the", 
        "weak", "through", "the", "valley", "of", "the", "darkness"
    ]

def test_get_sentences():
    assert analyzer.get_sentences() == [sample_text]

def test_get_preprocessed_text():
    assert analyzer.preprocessed_text == "blessed charity good shepherd weak valley darkness"

def test_get_preprocessed_words():
    assert analyzer.preprocessed_words == [
        "blessed", "charity", "good", "shepherd", "weak", 
        "valley", "darkness"
    ]

def test_generate_analysis():
    analyzer.plug_modules(["text"])
    result = analyzer.generate_analysis()
    assert result["text"]["character_count"] == 111
    assert result["text"]["character_per_word"] == 5.29
    assert result["text"]["word_count"] == 21
    assert result["text"]["paragraph_count"] == 1
    assert result["text"]["words_per_paragraph"] == 21.0
    assert result["text"]["sentences_per_paragraph"] == 1.0
    assert result["text"]["sentence_count"] == 1
    assert result["text"]["words_per_sentence"] == 21.0
    assert result["text"]["unique_word_count"] == 17