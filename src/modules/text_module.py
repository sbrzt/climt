import nltk
import string
import warnings
from collections import Counter
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import BlanklineTokenizer
from nltk.tokenize import SyllableTokenizer
from src.modules.analysis_module import AnalysisModule


# Ensure required NLTK resources are downloaded
# Uncomment them the first time and run to download them
# Then you can re-comment them
"""
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('vader_lexicon')
"""
warnings.filterwarnings("ignore", category=UserWarning, message="Character not defined in sonority_hierarchy")


class TextModule(AnalysisModule):
    """
    The TextModule class extends the AnalysisModule class and provides various text analysis functionalities. 
    It computes several statistics about the text such as character count, word count, sentence count, 
    paragraph count, syllable count, average characters per word, syllables per word, and more.

    This class assumes that the `analyzer` object passed to it has methods to retrieve the text, words, and sentences 
    from the text for analysis.
    """
    
    def __init__(self, analyzer):
        super().__init__(analyzer, "text_module")


    def get_character_count(self) -> int:
        """
        Returns the total number of characters in the text.

        Returns:
            int: The character count.
        """
        text = self.analyzer.get_text()
        character_count = len(text)
        return character_count


    def get_character_per_word(self) -> int:
        """
        Calculates the average number of characters per word.

        Returns:
            float: The average characters per word.
        """
        character_count = self.get_character_count()
        word_count = self.get_word_count()
        average = round(character_count / word_count, 2)
        return average


    def get_syllable_count(self) -> int:
        """
        Returns the total number of syllables in the text using a syllable tokenizer.

        Returns:
            int: The syllable count.
        """
        SSP = SyllableTokenizer()
        syllables = SSP.tokenize(self.analyzer.get_text())
        syllables_count = len(syllables)
        return syllables_count
    

    def get_syllable_count_per_word(self) -> float:
        """
        Calculates the average number of syllables per word.

        Returns:
            float: The average syllables per word.
        """
        syllable_count = self.get_syllable_count()
        word_count = self.get_word_count()
        average = round(syllable_count / word_count, 2)
        return average

    
    def get_word_count(self) -> int:
        """
        Returns the total number of words in the text.

        Returns:
            int: The word count.
        """
        words = self.analyzer.get_words()
        word_count = len(words)
        return word_count

    
    def get_paragraphs(self) -> list:
        """
        Tokenizes the text into paragraphs and assigns an ID to each paragraph.

        Returns:
            list: A list of dictionaries where each dictionary represents a paragraph 
                  with an 'id' and 'content' key.
        """
        text = self.analyzer.get_text()
        paragraph_list = BlanklineTokenizer().tokenize(text)
        paragraph_dict_list = [{'id': i, 'content': paragraph} for i, paragraph in enumerate(paragraph_list, 1)]
        return paragraph_dict_list


    def get_paragraph_count(self) -> int:
        """
        Returns the number of paragraphs in the text.

        Returns:
            int: The paragraph count.
        """
        paragraphs = self.get_paragraphs()
        paragraph_count = len(paragraphs)
        return paragraph_count


    def get_sentence_count(self) -> int:
        """
        Returns the total number of sentences in the text.

        Returns:
            int: The sentence count.
        """
        sentences = self.analyzer.get_sentences()
        sentence_count = len(sentences)
        return sentence_count


    def get_word_count_per_sentence(self) -> float:
        """
        Calculates the average number of words per sentence.

        Returns:
            float: The average word count per sentence.
        """
        word_count = self.get_word_count()
        sentence_count = self.get_sentence_count()
        return word_count / sentence_count


    def get_word_count_per_paragraph(self) -> float:
        """
        Calculates the average number of words per paragraph.

        Returns:
            float: The average word count per paragraph.
        """
        word_count = self.get_word_count()
        paragraph_count = self.get_paragraph_count()
        return word_count / paragraph_count


    def get_sentence_count_per_paragraph(self) -> float:
        """
        Calculates the average number of sentences per paragraph.

        Returns:
            float: The average sentence count per paragraph.
        """
        sentence_count = self.get_sentence_count()
        paragraph_count = self.get_paragraph_count()
        return sentence_count / paragraph_count


    def get_unique_word_count(self) -> int:
        """
        Returns the number of unique words in the text.

        Returns:
            int: The unique word count.
        """
        words = self.analyzer.get_words()
        unique_words = set(words)
        unique_word_count = len(unique_words)
        return unique_word_count


    def analyze(self) -> dict:
        """
        Collects and returns various statistics about the text, including character count, 
        word count, paragraph count, and more.

        Returns:
            dict: A dictionary containing various text statistics.
        """
        text_analysis = {
            'character_count': self.get_character_count(),
            'character_per_word': self.get_character_per_word(),
            'syllable_count': self.get_syllable_count(),
            'syllables_per_word': self.get_syllable_count_per_word(),
            'word_count': self.get_word_count(),
            'paragraph_count': self.get_paragraph_count(),
            'words_per_paragraph': self.get_word_count_per_paragraph(),
            'sentences_per_paragraph': self.get_sentence_count_per_paragraph(),
            'sentence_count': self.get_sentence_count(),
            'words_per_sentence': self.get_word_count_per_sentence(),
            'unique_word_count': self.get_unique_word_count(),
        }
        return text_analysis

