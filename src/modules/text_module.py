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
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download('vader_lexicon')
warnings.filterwarnings("ignore", category=UserWarning, message="Character not defined in sonority_hierarchy")


class TextModule(AnalysisModule):
    """
    """
    
    def __init__(self, analyzer):
        """
        """
        super().__init__(analyzer, "text_module")

        self.words = self.tokenize_text()
        self.preprocessed_text = self.preprocess_text(remove_stopwords=True, lemmatization=True)
        self.preprocessed_words = self.tokenize_preprocessed_text()


    def get_text(self):
        text = self.analyzer.text
        return text


    def get_character_count(self) -> int:
        """
        Returns the total number of characters in the text.

        Returns:
            int: The character count.
        """
        text = self.get_text()
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
        syllables = SSP.tokenize(self.get_text())
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
        text = self.get_text()
        sentences = self.get_sentences()
        #[{'id': i, 'content': word} for i, word in enumerate(sentence, 1)]
        tokens = [word for sentence in sentences for word in nltk.word_tokenize(sentence['content']) if word.isalpha()]
        return tokens


    def get_words(self) -> list:
        """
        Returns the tokenized words of the original text.

        Returns:
            list: A list of words.
        """
        words = self.words
        return words


    def get_preprocessed_text(self):
        preprocessed_text = self.preprocessed_text
        return preprocessed_text


    def tokenize_preprocessed_text(self) -> list:
        """
        Tokenizes the preprocessed text into words.

        Returns:
            list: A list of preprocessed words.
        """
        preprocessed_text = self.get_preprocessed_text()
        preprocessed_words = nltk.word_tokenize(preprocessed_text)
        return preprocessed_words


    def get_preprocessed_words(self) -> list:
        """
        Returns the tokenized words from the preprocessed text.

        Returns:
            list: A list of preprocessed words.
        """
        preprocessed_words = self.preprocessed_words
        return preprocessed_words

    
    def get_word_count(self) -> int:
        """
        Returns the total number of words in the text.

        Returns:
            int: The word count.
        """
        words = self.get_words()
        word_count = len(words)
        return word_count

    
    def get_paragraphs(self) -> list:
        """
        Tokenizes the text into paragraphs and assigns an ID to each paragraph.

        Returns:
            list: A list of dictionaries where each dictionary represents a paragraph 
                  with an 'id' and 'content' key.
        """
        text = self.get_text()
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

    
    def get_sentences(self) -> list:
        """
        Tokenizes the text into sentences.

        Returns:
            list: A list of sentences.
        """
        text = self.get_text()
        sentence_list = nltk.sent_tokenize(text)
        sentence_dict_list = [{'id': i, 'content': sentence} for i, sentence in enumerate(sentence_list, 1)]
        return sentence_dict_list


    def get_sentence_count(self) -> int:
        """
        Returns the total number of sentences in the text.

        Returns:
            int: The sentence count.
        """
        sentences = self.get_sentences()
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
        words = self.get_words()
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

