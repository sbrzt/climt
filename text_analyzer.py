import nltk
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import BlanklineTokenizer
from nltk.tokenize import SyllableTokenizer
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
        self.text = text
        self.preprocessed_text = self.preprocess_text(remove_stopwords=True, lemmatization=True)
        self.analysis = self.text_statistics()

    
    def get_character_count(self) -> int:
        '''
        Get the total number of characters in the text.
        Output:
            - a integer representing the total number of characters
        '''
        return len(self.text)


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
        syllables = SSP.tokenize(self.text)
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
        text = self.text.lower()

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
        return nltk.word_tokenize(self.text)


    def get_word_count(self) -> int:
        '''
        Get the total number of words in the stext.
        Output:
            - a integer representing the total number of words
        '''
        return len(self.get_words())

    
    def get_paragraphs(self) -> list:
        '''
        Get the paragraphs contained in the text.
        Output:
            - a list of strings, each representing a single paragraph
        '''
        paragraphs = BlanklineTokenizer().tokenize(self.text)
        return paragraphs

    
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
        return nltk.sent_tokenize(self.text)


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
        return Counter(self.preprocessed_text).most_common(50)


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


    #######################################################
    #######################################################
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


    def get_polarity_scores(self, text):
        '''
        Return the polarity scores assigned to the text.

        Input:
            - text: a string representing the text

        Output:
            - a dictionary consisting in four score-value pairs (compound, negative, neutral and positive)
        '''
        sia = SentimentIntensityAnalyzer()
        return sia.polarity_scores(text)


    def text_statistics(self):
        '''
        Return a basic quantitative analysis of the text, consisting in a character count, a word count, a sentence count, and a word per sentence count.

        Output:
            - a dictionary containing a character count, a word count, a sentence count, and a word per sentence count
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
    

    def text_composition(self):
        '''
        Return a detailed analysis for each word in the text, including its number of occurrences, frequency, PoS tag and possible senses.

        Output:
            - a list of dictionaries, each representing a single word analysis
        '''
        counts = Counter(tag for word, tag in self.__word_pos)
        adjective_count = counts['JJ']
        adverb_count = counts['RB'] + counts['RBR'] + counts['RBS'] + counts['WRB']
        conjunction_count = counts['CC'] + counts['IN']
        determiner_count = counts['DT']
        noun_count = counts['NN'] + counts['NNS']
        proper_noun_count = counts['NNP'] + counts['NNPS']
        preposition_count = counts['IN'] + counts['PP']
        pronoun_count = counts['PRP'] + counts['PRP$'] + counts['WP'] + counts['WP$']
        verb_count = counts['VBD'] + counts['VBG'] + counts['VBN'] + counts['VBP'] + counts['VBZ'] + counts['VP']
        text_composition_analysis = {
            'adjectives': adjective_count,
            'adverbs': adverb_count,
            'conjunctions': conjunction_count,
            'determiners': determiner_count,
            'nouns': noun_count,
            'proper_nouns': proper_noun_count,
            'prepositions': preposition_count,
            'pronouns': pronoun_count,
            'verbs': verb_count
        }        
        '''word_details = []
        for word, count in self.__most_common_word_frequencies:
            frequency_percent = (count / self.__word_count) * 100
            pos_tag = dict(self.__word_pos).get(word, 'N/A')
            synsets = wn.synsets(word, pos=self.__get_wordnet_pos(pos_tag))
            senses = [synset.definition() for synset in synsets]
            word_details.append({
                'word': word,
                'occurrences': count,
                'frequency_percent': frequency_percent,
                'pos_tag': pos_tag,
                'senses': senses
            })
        return word_details'''
        return text_composition_analysis


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
            'text_standard': textstat.text_standard(self.__text),
            'reading_time': f'{self.__word_count / 225} min.',
            'speaking_time': f'{self.__word_count / 125} min.'
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
        ### tone 
        ### personalism
        
        ###
        ### USE DATAFRAME AND CONVERT IT TO DICT AT THE END?????
        ###
        sia = SentimentIntensityAnalyzer()
        threshold = 0
        '''
        sentences_analyzed = []
        for sentence in self.__sentences:
            polarity_scores = sia.polarity_scores(sentence)
            #polarity_scores['sentence'] = sentence
            sentiment = 1 if polarity_scores['compound'] > threshold else 0
            sentences_analyzed.append((sentence, sentiment))
        return sentences_analyzed
        '''
        polarity_scores = sia.polarity_scores(self.preprocessed_text)
        return polarity_scores


    def analyze(self, focus):
        '''
        Construct and return a full analysis, based on the analysis focus.

        Input:
            - focus: a string representing the focus of the analysis 
        
        Output:
            - a dictionary representing the full analysis
        '''
        if 'text' in focus:
            self.analysis['text_composition'] = self.text_composition()
        if 'word' in focus:
            pass
        if 'read' in focus:
            self.analysis['readibility_analysis'] = self.readibility_analysis()
        if 'ngram' in focus:
            self.analysis['ngram_analysis'] = self.ngram_analysis()
        if 'ner' in focus:
            self.analysis['ner_analysis'] = self.named_entity_analysis()
        if 'sentiment' in focus:
            self.analysis['sentiment_analysis'] = self.sentiment_analysis()
        return self.analysis
