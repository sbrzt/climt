import nltk
import string
import warnings
from modules.composition_module import CompositionModule
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
    '''
    A class designed for text analysis, enabling various quantitative and qualitative linguistic assessments.
    '''

    def __init__(self, text):
        self.text = text
        self.preprocessed_text = self.preprocess_text(remove_stopwords=True, lemmatization=True)
        self.analysis = self.text_statistics()

    
    def get_text(self):
        return self.text

    
    def get_character_count(self) -> int:
        '''
        Get the total number of characters in the text.
        Output:
            - a integer representing the total number of characters
        '''
        return len(self.get_text())


    def get_character_per_word(self) -> int:
        '''
        Get the average number of characters per word in the text.
        Output:
            - a integer representing the average number of characters per word in the text
        '''
        return self.get_character_count() / len(self.get_words())

    
    def get_syllable_count(self) -> int:
        '''
        Get the total number of syllables in the text.
        Output:
            - a integer representing the total number of syllables
        '''
        SSP = SyllableTokenizer()
        syllables = SSP.tokenize(self.get_text())
        return len(syllables)

    
    def get_syllable_count_per_word(self) -> float:
        '''
        Get the average number of syllables per word in the text.
        Output:
            - a float representing the average number of syllables per word
        '''
        return self.get_syllable_count() / self.get_word_count()


    def preprocess_text(self, remove_stopwords=False, stemming=False, lemmatization=False) -> str:
        '''
        Preprocess the input text by converting to lowercase and removing punctuation.
        Output:
            - a string representing the processed text
        '''
        # Lower casing
        text = self.get_text().lower()

        # Punctuation removal
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Stopwords removal
        if remove_stopwords == True:
            STOPWORDS = set(stopwords.words('english'))
            text = " ".join([word for word in str(text).split() if word not in STOPWORDS])

        # Stemming
        if stemming == True:
            stemmer = PorterStemmer()
            text = " ".join([stemmer.stem(word) for word in text.split()])

        # Lemmatization
        if lemmatization == True:
            lemmatizer = WordNetLemmatizer()
            text = " ".join([lemmatizer.lemmatize(word) for word in text.split()])

        return text


    def get_words(self) -> list:
        '''
        Get the words contained in the text.
        Output:
            - a list of strings, each representing a single word
        '''
        return nltk.word_tokenize(self.get_text())


    def get_preprocessed_words(self) -> list:
        '''
        Get the words contained in the preprocessed text.
        Output:
            - a list of strings, each representing a single word
        '''
        return nltk.word_tokenize(self.preprocessed_text)


    def get_word_count(self) -> int:
        '''
        Get the total number of words in the text.
        Output:
            - a integer representing the total number of words
        '''
        return len(self.get_words())

    
    def get_paragraphs(self) -> list:
        '''
        Get the paragraphs contained in the text.
        Output:
            - ...
        '''
        paragraph_list = BlanklineTokenizer().tokenize(self.get_text())
        paragraph_dict = [{'id': i, 'content': paragraph} for i, paragraph in enumerate(paragraph_list, 1)]
        return paragraph_dict

    
    def get_paragraph_count(self) -> int:
        '''
        Get the number of paragraphs contained in the text. 
        Output:
            - a integer, representing the total number of paragraphs
        '''
        return len(self.get_paragraphs())


    def get_sentences(self) -> list:
        '''
        Get the sentences contained in the text.
        Output:
            - a list of strings, each representing a sentence
        '''
        return nltk.sent_tokenize(self.get_text())


    def get_sentence_count(self) -> int:
        '''
        Get the total number of sentences in the text.
        Output:
            - a integer representing the total number of sentences
        '''
        return len(self.get_sentences())


    def get_word_count_per_sentence(self) -> float:
        '''
        Get the average number of words per sentence in the text.
        Output:
            - a float representing the average number of words per sentence
        '''
        return self.get_word_count() / self.get_sentence_count()

    
    def get_word_count_per_paragraph(self) -> float:
        '''
        Get the average number of words per paragraph in the text.
        Output:
            - a float representing the average number of words per paragraph
        '''
        return self.get_word_count() / self.get_paragraph_count()

    
    def get_sentence_count_per_paragraph(self) -> float:
        '''
        Get the average number of sentences per paragraph in the text.
        Output:
            - a float representing the average number of sentences per paragraph
        '''
        return self.get_sentence_count() / self.get_paragraph_count()


    def get_most_common_word_frequencies(self) -> list:
        '''
        Return a list of word-frequency pairs of the N most common words in the text.
        Output:
            - a list of tuples, each representing a word-frequency pair
        '''
        return Counter(self.get_preprocessed_words()).most_common(50)


    def get_word_pos(self) -> list:
        '''
        Get the Part of Speech (PoS) tag for each word in the text.
        Output:
            - a list of word-PoS tag pairs
        '''
        return nltk.pos_tag(self.get_words())


    def get_unique_word_count(self) -> int:
        '''
        Get the total number of unique words in the stext.        
        Output:
            - a integer representing the total number of unique words
        '''
        return len(set(self.get_words()))


    def get_type_token_ratio(self) -> float:
        '''
        Get the ratio of unique words (types) to total words (tokens).
        Output:
            - a float representing the type-token ratio
        '''
        return self.get_unique_word_count() / self.get_word_count()


    def text_statistics(self):
        '''
        Return a basic quantitative analysis of the text.

        Output:
            - a dictionary
        '''
        return {
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


    def analyze(self, focus):
        '''
        Construct and return a full analysis, based on the analysis focus.

        Input:
            - focus: a string representing the focus of the analysis 
        
        Output:
            - a dictionary representing the full analysis
        '''
        if 'text' in focus:
            composition_module = CompositionModule(self)
            self.analysis['text_composition'] = composition_module.analyze()
        if 'read' in focus:
            readability_module = ReadabilityModule(self)
            self.analysis['readability_analysis'] = readability_module.analyze()
        if 'sentiment' in focus:
            sentiment_module = SentimentModule(self)
            self.analysis['sentiment_analysis'] = sentiment_module.analyze()
        return self.analysis
