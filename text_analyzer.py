# Type-Token Ratio (TTR): Ratio of unique words (types) to total words (tokens).
# Readability scores
# Common Bigrams: Most frequent pairs of consecutive words.
# Common Trigrams: Most frequent triplets of consecutive words.
# Entities: List of named entities (e.g., persons, locations, organizations) and their frequencies.
# Sentiment Score: Overall sentiment score of the text (e.g., positive, neutral, negative).


import nltk
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import textstat

# Ensure required NLTK resources are downloaded
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')

class TextAnalyzer:
    '''
    description of class
    '''

    def __init__(self, text):
        self.__text = text
        self.__char_count = self.get_char_count(self.__text)
        self.__text_preprocessed = self.__preprocess_text(self.__text)
        self.__text_lemmatized = self.__preprocess_text(self.__text, remove_stopwords=True, lemmatization=True)
        self.__words = self.get_words(self.__text_preprocessed)
        self.__lemmas = self.get_words(self.__text_lemmatized)
        self.__word_count = self.get_word_count(self.__words)
        self.__sentences = self.get_sentences(self.__text)
        self.__sentence_count = self.get_sentence_count(self.__sentences)
        self.__word_count_per_sentence = self.get_word_count_per_sentence(self.__word_count, self.__sentence_count)
        self.__most_common_word_frequencies = self.get_most_common_word_frequencies(self.__lemmas)
        self.__word_pos = self.get_word_pos(self.__lemmas)

        self.analysis = self.core_analysis()

    
    def get_char_count(self, text: str) -> int:
        '''
        Get the total number of characters in the text.

        Input:
            - text: a string representing the text

        Output:
            - a integer representing the total number of characters
        '''
        return len(text)

    def __preprocess_text(self, text: str, remove_stopwords=False, stemming=False, lemmatization=False) -> str:
        '''
        Preprocess the input text by converting to lowercase and removing punctuation.

        Input:
            - text: a string representing the text to be processed

        Output:
            - a string representing the processed text
        '''

        # Lower casing
        text = text.lower()

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

    def get_words(self, text: str) -> list:
        '''
        Get the words contained in the text.

        Input:
            - text: a string representing the text
        
        Output:
            - a list of strings, each representing a single word
        '''
        return nltk.word_tokenize(text)

    def get_word_count(self, words: list) -> int:
        '''
        Get the total number of words in the stext.

        Input:
            - words: list of strings, each representing a word
        
        Output:
            - a integer representing the total number of words
        '''
        return len(words)

    def get_sentences(self, text: str) -> list:
        '''
        Get the sentences contained in the text.

        Input:
            - text: a string representing the text

        Output:
            - a list of strings, each representing a sentence
        '''
        return nltk.sent_tokenize(text)

    def get_sentence_count(self, sentences: list) -> int:
        '''
        Get the total number of sentences in the text.

        Input:
            - sentences: a list of strings, each representing a sentence
        
        Output:
            - a integer representing the total number of sentences
        '''
        return len(sentences)

    def get_word_count_per_sentence(self, word_count: int, sentence_count: int) -> float:
        '''
        Get the average number of words per sentence in the text.

        Input:
            - word_count: a integer representing the total number of words in the text
            - sentence_count: a integer representing the total number of sentences in the text

        Output:
            - a float representing the average number of words per sentence
        '''
        return word_count / sentence_count

    def get_most_common_word_frequencies(self, text):
        '''
        Return a list of word-frequency pairs of the N most common words in the text.

        Input:
            - text: a string representing the text

        Output:
            - a list of tuples, each representing a word-frequency pair
        '''
        return Counter(text).most_common(50)

    def get_word_pos(self, words):
        '''
        Get the Part of Speech (PoS) tag for each word in the text.

        Input:
            - words: a list of strings, each representing a word in the text

        Output:
            - a dictionary of word-PoS tag pairs
        '''
        return dict(nltk.pos_tag(words))

    def __get_wordnet_pos(self, tag):
        '''
        Convert NLTK PoS tags into WordNet PoS tags.

        Input:
            - tag: a string representing a NLTK PoS tag

        Output:
            - a WordNet PoS tag
        '''
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


    def core_analysis(self):
        '''
        Return a basic quantitative analysis of the text, consisting in a character count, a word count, a sentence count, and a word per sentence count.

        Output:
            - a dictionary containing a character count, a word count, a sentence count, and a word per sentence count
        '''
        return {
            'char_count': self.__char_count,
            'word_count': self.__word_count,
            'sentence_count': self.__sentence_count,
            'words_per_sentence': self.__word_count_per_sentence,
        }
    
    def word_analysis(self):
        '''
        Return a more detailed analysis for each word in the text, including its number of occurrences, frequency, PoS tag and possible senses.

        Output:
            - a list of dictionaries, each representing a single word analysis
        '''
        word_details = []
        for word, count in self.__most_common_word_frequencies:
            frequency_percent = (count / self.__word_count) * 100
            pos_tag = self.__word_pos.get(word, 'N/A')
            synsets = wn.synsets(word, pos=self.__get_wordnet_pos(pos_tag))
            senses = [synset.definition() for synset in synsets]
            word_details.append({
                'word': word,
                'occurrences': count,
                'frequency_percent': frequency_percent,
                'pos_tag': pos_tag,
                'senses': senses
            })
        return word_details


    def analyze(self, focus):
        '''
        Construct and return a full analysis, based on the analysis focus.

        Input:
            - focus: a string representing the focus of the analysis 
        
        Output:
            - a dictionary representing the full analysis
        '''
        if 'word' in focus:
            self.analysis['word_details'] = self.word_analysis()
        return self.analysis
