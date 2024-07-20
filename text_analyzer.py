import nltk
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.sentiment import SentimentIntensityAnalyzer
import textstat

# Ensure required NLTK resources are downloaded
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download('vader_lexicon')

class TextAnalyzer:
    '''
    A class designed for text analysis, enabling various quantitative and qualitative linguistic assessments.
    '''

    def __init__(self, text):
        self.__text = text
        self.__char_count = self.get_char_count(self.__text)
        self.__text_preprocessed = self.__preprocess_text(self.__text)
        self.__text_lemmatized = self.__preprocess_text(self.__text, remove_stopwords=True, lemmatization=True)
        self.__words = self.get_words(self.__text_preprocessed)
        self.__char_per_word = self.get_char_per_word(self.__words)
        self.__lemmas = self.get_words(self.__text_lemmatized)
        self.__word_count = self.get_word_count(self.__words)
        self.__sentences = self.get_sentences(self.__text)
        self.__sentence_count = self.get_sentence_count(self.__sentences)
        self.__word_count_per_sentence = self.get_word_count_per_sentence(self.__word_count, self.__sentence_count)
        self.__most_common_word_frequencies = self.get_most_common_word_frequencies(self.__lemmas)
        self.__word_pos = self.get_word_pos(self.__lemmas)
        self.__type_token_ratio = self.get_type_token_ratio(self.__words, self.__word_count)

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


    def get_char_per_word(self, words: list) -> int:
        '''
        Get the average number of characters per word in the text.

        Input:
            - words: list of strings, each representing a word

        Output:
            - a integer representing the average number of characters per word in the text
        '''
        total_chars = sum(len(word) for word in words)
        total_words = len(words)
        average_chars_per_word = total_chars / total_words if total_words > 0 else 0
        return average_chars_per_word


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


    def get_type_token_ratio(self, words, word_count):
        '''
        Get the ratio of unique words (types) to total words (tokens).

        Input:
            - words: a list of strings, each representing a word in the text
            - word_count: a integer representing the total number of words in the text

        Output:
            - a integer representing the type-token ratio
        '''
        return len(set(words)) / word_count


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


    def __get_most_frequent_ngrams(self, words, n=2, top_k=10):
        '''
        Return the most frequent N-grams of a specified length in the text.

        Input:
            - words: a list of strings, each representing a word
            - n: a integer, representing the number of adjacent symbols in each sequence (n=2 by default)
            - top_k: a integer, representing the number of most frequent N-grams to be returned (top_k=10 by default)
        
        Output:
            - a list of tuples, each representing a N-gram-count pair
        '''
        ngrams = nltk.ngrams(words, n)
        ngram_freq = Counter(ngrams)
        return ngram_freq.most_common(top_k)


    def __get_named_entities(self, words):
        '''
        Return the list of named entities referenced in the text.

        Input:
            - words: a list of strings, each representing a wrod
        
        Output:
            - a list of tuples, each representing a named entity and its type
        '''
        parse_tree = nltk.ne_chunk(nltk.pos_tag(words))
        named_entities_set = []
        for t in parse_tree.subtrees():
            if t.label() == "ORGANIZATION" or t.label() == "PERSON" or t.label() == "GPE":
                named_entities_set.append((t.label(), ' '.join(c[0] for c in t)))
        return named_entities_set


    def __get_polarity_scores(self, text):
        '''
        Return the polarity scores assigned to the text.

        Input:
            - text: a string representing the text

        Output:
            - a dictionary consisting in four score-value pairs (compound, negative, neutral and positive)
        '''
        sia = SentimentIntensityAnalyzer()
        return sia.polarity_scores(text)


    def core_analysis(self):
        '''
        Return a basic quantitative analysis of the text, consisting in a character count, a word count, a sentence count, and a word per sentence count.

        Output:
            - a dictionary containing a character count, a word count, a sentence count, and a word per sentence count
        '''
        ### syllable count
        ### syllables per word
        ### paragraph count
        ### words per paragraph
        ### sentences per paragraph
        ### unique word count
        ### reading time (at 225 words per minute)
        ### speaking time (at 125 words per minute)
        return {
            'char_count': self.__char_count,
            'char_per_word': self.__char_per_word,
            'word_count': self.__word_count,
            'sentence_count': self.__sentence_count,
            'words_per_sentence': self.__word_count_per_sentence,
            'type_token_ratio': self.__type_token_ratio
        }
    
    def word_analysis(self):
        '''
        Return a detailed analysis for each word in the text, including its number of occurrences, frequency, PoS tag and possible senses.

        Output:
            - a list of dictionaries, each representing a single word analysis
        '''
        ### adjectives
        ### adverbs
        ### conjunctions
        ### determiners
        ### interjections
        ### nouns
        ### proper nouns
        ### prepositions
        ### pronouns
        ### qualifiers
        ### verbs
        
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

    def readibility_analysis(self):
        '''
        Return a detailed analysis for the readibility of the text in terms of scores, each based on a specific metric (e.g. Flesch-Kincaid Grade, Automated Readibility Index, etc.)
        
        Output:
            - a dictionary representing the readibility analysis
        '''
        readability_scores = {
            'flesch_reading_ease': textstat.flesch_reading_ease(self.__text),
            'smog_index': textstat.smog_index(self.__text),
            'flesch_kincaid_grade': textstat.flesch_kincaid_grade(self.__text),
            'coleman_liau_index': textstat.coleman_liau_index(self.__text),
            'automated_readability_index': textstat.automated_readability_index(self.__text),
            'dale_chall_readability_score': textstat.dale_chall_readability_score(self.__text),
            'difficult_words': textstat.difficult_words(self.__text),
            'linsear_write_formula': textstat.linsear_write_formula(self.__text),
            'gunning_fog': textstat.gunning_fog(self.__text),
            'text_standard': textstat.text_standard(self.__text)
        }
        ### sentences > 30 syllables
        ### words > 12 letters
        ### adverb count < 4%
        ### passive voice count
        
        return readability_scores

    def ngram_analysis(self):
        '''
        Return a detailed analysis for the most frequent N-grams in the text.

        Output:
            - a dictionary, representing the N-grams analysis.
        '''
        return dict(self.__get_most_frequent_ngrams(self.__words))

    def named_entity_analysis(self):
        '''
        Return a detailed analysis for the named entities recognition in the text. 

        Output:
            - a dictionary representing the named entity analysis

        '''
        return self.__get_named_entities(self.get_words(self.__text))

    def sentiment_analysis(self):
        '''
        Return a detailed analysis for the sentiment polarities for each sentence in the text. 

        Output:
            - a dictionary representing the sentiment analysis
        '''
        ### reach
        ### tone 
        ### personalism
        sentences_analyzed = []
        for sentence in self.__sentences:
            polarity_scores = self.__get_polarity_scores(sentence)
            polarity_scores['sentence'] = sentence
            sentences_analyzed.append(polarity_scores)
        return sentences_analyzed

    def analyze(self, focus):
        '''
        Construct and return a full analysis, based on the analysis focus.

        Input:
            - focus: a string representing the focus of the analysis 
        
        Output:
            - a dictionary representing the full analysis
        '''
        if 'word' in focus:
            self.analysis['word_analysis'] = self.word_analysis()
        if 'read' in focus:
            self.analysis['readibility_analysis'] = self.readibility_analysis()
        if 'ngram' in focus:
            self.analysis['ngram_analysis'] = self.ngram_analysis()
        if 'ner' in focus:
            self.analysis['ner_analysis'] = self.named_entity_analysis()
        if 'sentiment' in focus:
            self.analysis['sentiment_analysis'] = self.sentiment_analysis()
        return self.analysis
