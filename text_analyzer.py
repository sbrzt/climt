import nltk
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn

# Ensure required NLTK resources are downloaded
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.__words = self.preprocess_text(text)
        self.__sentences = nltk.sent_tokenize(text)
        self.char_count = len(text)
        self.word_count = len(self.__words)
        self.sentence_count = len(self.__sentences)
        self.syllables_count = sum(len([char for char in word if char in "aeiou"]) for word in self.__words)
        self.syllables_per_word = self.syllables_count / self.word_count
        self.words_per_sentence = self.word_count / self.sentence_count
        self.flesch_kincaid_score = 206.835 - (1.015 * self.words_per_sentence) - (84.6 * self.syllables_per_word)
        self.analysis = self.core_analysis()

    def preprocess_text(self, text):
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = nltk.word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word not in stop_words]
        return words

    def get_wordnet_pos(self, tag):
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
        return {
            'char_count': self.char_count,
            'word_count': self.word_count,
            'sentence_count': self.sentence_count,
            'syllables_count': self.syllables_count,
            'syllables_per_word': self.syllables_per_word,
            'words_per_sentence': self.words_per_sentence,
            'flesch_kincaid_score': self.flesch_kincaid_score
        }

    def word_analysis(self):
        lemmatizer = nltk.WordNetLemmatizer()
        word_freq = Counter(self.__words).most_common(50)
        pos_tags = dict(nltk.pos_tag(self.__words))
        word_details = []
        for word, count in word_freq:
            frequency_percent = (count / self.word_count) * 100
            pos_tag = pos_tags.get(word, 'N/A')
            wordnet_pos = self.get_wordnet_pos(pos_tag) or wn.NOUN
            lemma = lemmatizer.lemmatize(word, pos=wordnet_pos)
            synsets = wn.synsets(word, pos=wordnet_pos)
            senses = [synset.definition() for synset in synsets]
            word_details.append({
                'word': word,
                'occurrences': count,
                'frequency_percent': frequency_percent,
                'pos_tag': wordnet_pos,
                'lemma': lemma,
                'senses': senses
            })
        return word_details


    # Type-Token Ratio (TTR): Ratio of unique words (types) to total words (tokens).

    # Common Bigrams: Most frequent pairs of consecutive words.
    # Common Trigrams: Most frequent triplets of consecutive words.

    # Entities: List of named entities (e.g., persons, locations, organizations) and their frequencies.

    # Sentiment Score: Overall sentiment score of the text (e.g., positive, neutral, negative).


    def analyze(self, focus):
        if 'word' in focus:
            self.analysis['word_details'] = self.word_analysis()
        return self.analysis
