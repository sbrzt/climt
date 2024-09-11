import nltk
import string
import warnings
from collections import Counter
from modules.composition_module import CompositionModule
from modules.word_module import WordModule
from modules.readability_module import ReadabilityModule
from modules.sentiment_module import SentimentModule
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import BlanklineTokenizer
from nltk.tokenize import SyllableTokenizer

# Ensure required NLTK resources are downloaded
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download('vader_lexicon')
warnings.filterwarnings("ignore", category=UserWarning, message="Character not defined in sonority_hierarchy")


class TextAnalyzer():
    """
    A class for analyzing text data. This class provides methods for performing various 
    text preprocessing tasks, tokenization, and statistical analysis of the text, such as 
    word and character counts, syllable counts, and more.

    Attributes:
        text (str): The input text to be analyzed.
        words (list): Tokenized words from the original text.
        preprocessed_text (str): Text after preprocessing (e.g., stopword removal, lemmatization).
        preprocessed_words (list): Tokenized words from the preprocessed text.
        analysis (dict): Dictionary containing statistical analysis of the text.
    """

    def __init__(self, text):
        """
        Initializes the TextAnalyzer with the input text and performs tokenization, 
        preprocessing, and text statistics calculation.

        Args:
            text (str): The input text to be analyzed.
        """
        self.text = text
        self.words = self.tokenize_text()
        self.preprocessed_text = self.preprocess_text(remove_stopwords=True, lemmatization=True)
        self.preprocessed_words = self.tokenize_preprocessed_text()
        self.analysis = self.text_statistics()

    
    def get_text(self) -> str:
        """
        Returns the original text.

        Returns:
            str: The input text.
        """
        return self.text

    
    def get_character_count(self) -> int:
        """
        Returns the total number of characters in the text.

        Returns:
            int: The character count.
        """
        return len(self.get_text())


    def get_character_per_word(self) -> int:
        """
        Calculates the average number of characters per word.

        Returns:
            float: The average characters per word.
        """
        return self.get_character_count() / len(self.get_words())

    
    def get_syllable_count(self) -> int:
        """
        Returns the total number of syllables in the text using a syllable tokenizer.

        Returns:
            int: The syllable count.
        """
        SSP = SyllableTokenizer()
        syllables = SSP.tokenize(self.get_text())
        return len(syllables)

    
    def get_syllable_count_per_word(self) -> float:
        """
        Calculates the average number of syllables per word.

        Returns:
            float: The average syllables per word.
        """
        return self.get_syllable_count() / self.get_word_count()


    def preprocess_text(self, remove_stopwords=False, stemming=False, lemmatization=False) -> str:
        """
        Preprocesses the text by converting to lowercase, removing punctuation, and optionally 
        removing stopwords, stemming, and lemmatizing.

        Args:
            remove_stopwords (bool): Whether to remove stopwords.
            stemming (bool): Whether to apply stemming.
            lemmatization (bool): Whether to apply lemmatization.

        Returns:
            str: The preprocessed text.
        """
        text = self.get_text().lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

        if remove_stopwords == True:
            STOPWORDS = set(stopwords.words('english'))
            text = " ".join([word for word in str(text).split() if word not in STOPWORDS])

        if stemming == True:
            stemmer = PorterStemmer()
            text = " ".join([stemmer.stem(word) for word in text.split()])

        if lemmatization == True:
            lemmatizer = WordNetLemmatizer()
            text = " ".join([lemmatizer.lemmatize(word) for word in text.split()])

        return text


    def tokenize_text(self) -> list:
        """
        Tokenizes the original text into words.

        Returns:
            list: A list of words in the text.
        """
        words = nltk.word_tokenize(self.get_text())
        return words


    def get_words(self) -> list:
        """
        Returns the tokenized words of the original text.

        Returns:
            list: A list of words.
        """
        return self.words


    def tokenize_preprocessed_text(self) -> list:
        """
        Tokenizes the preprocessed text into words.

        Returns:
            list: A list of preprocessed words.
        """
        preprocessed_text = nltk.word_tokenize(self.preprocessed_text)
        return preprocessed_text


    def get_preprocessed_words(self) -> list:
        """
        Returns the tokenized words from the preprocessed text.

        Returns:
            list: A list of preprocessed words.
        """
        return self.preprocessed_words


    def get_word_count(self) -> int:
        """
        Returns the total number of words in the text.

        Returns:
            int: The word count.
        """
        return len(self.get_words())

    
    def get_paragraphs(self) -> list:
        """
        Tokenizes the text into paragraphs and assigns an ID to each paragraph.

        Returns:
            list: A list of dictionaries where each dictionary represents a paragraph 
                  with an 'id' and 'content' key.
        """
        paragraph_list = BlanklineTokenizer().tokenize(self.get_text())
        paragraph_dict = [{'id': i, 'content': paragraph} for i, paragraph in enumerate(paragraph_list, 1)]
        return paragraph_dict

    
    def get_paragraph_count(self) -> int:
        """
        Returns the number of paragraphs in the text.

        Returns:
            int: The paragraph count.
        """
        return len(self.get_paragraphs())


    def get_sentences(self) -> list:
        """
        Tokenizes the text into sentences.

        Returns:
            list: A list of sentences.
        """
        return nltk.sent_tokenize(self.get_text())


    def get_sentence_count(self) -> int:
        """
        Returns the total number of sentences in the text.

        Returns:
            int: The sentence count.
        """
        return len(self.get_sentences())


    def get_word_count_per_sentence(self) -> float:
        """
        Calculates the average number of words per sentence.

        Returns:
            float: The average word count per sentence.
        """
        return self.get_word_count() / self.get_sentence_count()

    
    def get_word_count_per_paragraph(self) -> float:
        """
        Calculates the average number of words per paragraph.

        Returns:
            float: The average word count per paragraph.
        """
        return self.get_word_count() / self.get_paragraph_count()

    
    def get_sentence_count_per_paragraph(self) -> float:
        """
        Calculates the average number of sentences per paragraph.

        Returns:
            float: The average sentence count per paragraph.
        """
        return self.get_sentence_count() / self.get_paragraph_count()


    def get_most_common_word_frequencies(self) -> list:
        """
        Returns the 50 most common words in the preprocessed text along with their frequencies.

        Returns:
            list: A list of tuples where each tuple contains a word and its frequency.
        """
        return Counter(self.get_preprocessed_words()).most_common(50)


    def get_word_pos(self) -> list:
        """
        Performs part-of-speech (POS) tagging on the tokenized words.

        Returns:
            list: A list of tuples where each tuple contains a word and its POS tag.
        """
        return nltk.pos_tag(self.get_words())

    
    def get_wordnet_pos(self, tag) -> str:
        """
        Maps a POS tag to the appropriate WordNet POS tag.

        Args:
            tag (str): The POS tag to map.

        Returns:
            str: The corresponding WordNet POS tag.
        """
        if tag.startswith('J'):
            return wn.ADJ
        elif tag.startswith('V'):
            return wn.VERB
        elif tag.startswith('N'):
            return wn.NOUN
        elif tag.startswith('R'):
            return wn.ADV
        else:
            return None


    def get_unique_word_count(self) -> int:
        """
        Returns the number of unique words in the text.

        Returns:
            int: The unique word count.
        """
        return len(set(self.get_words()))


    def get_type_token_ratio(self) -> float:
        """
        Calculates the type-token ratio (TTR), which is the ratio of unique words to the total word count.

        Returns:
            float: The type-token ratio.
        """
        return self.get_unique_word_count() / self.get_word_count()


    def text_statistics(self) -> dict:
        """
        Collects and returns various statistics about the text, including character count, 
        word count, paragraph count, and more.

        Returns:
            dict: A dictionary containing various text statistics.
        """
        statistics_analysis = {
            'text_statistics': {
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
                'type_token_ratio': self.get_type_token_ratio()
            }
        }
        return statistics_analysis


    def analyze(self, focus):
        """
        Analyzes the text based on the specified focus areas, such as text composition, 
        word analysis, readability, or sentiment.

        Args:
            focus (list): A list of focus areas to analyze (e.g., ['text', 'word', 'read', 'sentiment']).

        Returns:
            dict: A dictionary containing the analysis results for the specified focus areas.
        """
        if 'text' in focus:
            composition_module = CompositionModule(self)
            self.analysis['text_composition'] = composition_module.analyze()
        if 'word' in focus:
            word_module = WordModule(self)
            self.analysis['word_analysis'] = word_module.analyze()
        if 'read' in focus:
            readability_module = ReadabilityModule(self)
            self.analysis['readability_analysis'] = readability_module.analyze()
        if 'sentiment' in focus:
            sentiment_module = SentimentModule(self)
            self.analysis['sentiment_analysis'] = sentiment_module.analyze()
        return self.analysis
