import unittest
from src.text_analyzer import TextAnalyzer


class TestTextAnalyzer(unittest.TestCase):
    
    def test_get_text(self):
        text_analyzer = TextAnalyzer(
            "Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness. For he is truly his brother's keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy my brothers."
        )
        assert text_analyzer.get_text() == "Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness. For he is truly his brother's keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy my brothers."

    def test_get_character_count(self):
        text_analyzer = TextAnalyzer(
            "Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness. For he is truly his brother's keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy my brothers."
        )
        assert text_analyzer.get_character_count() == 306

    def test_get_words(self):
        text_analyzer = TextAnalyzer(
            "Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness."
        )
        print(text_analyzer.get_words())
        assert text_analyzer.get_words() == ["Blessed", "is", "he", "who", "in", "the", "name", "of", "charity", "and", "good", "will", "shepherds", "the", "weak", "through", "the", "valley", "of", "the", "darkness"]

    # get_word_count

    # get_character_per_word
    
    # get syllable_count

    # get_syllable_cout_per_word

    # get_sentences

    # get_sentence_count

    # get_word_count_per_sentence

    # get_paragraphs

    # get_paragraphs_count

    # get_word_count_per_paragraph

    # get_sentence_count_per_paragraph

    # preprocess_text

    # get_preprocessed_text

    # get_preprocessed_words

    # get_word_pos ##################################

    # get_wordnet_pos ###############################

    # get_unique_word_count

    # analyze

if __name__ == "__main__":
    unittest.main()