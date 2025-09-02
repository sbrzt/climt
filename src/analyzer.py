# analyzer.py

import nltk
import string
from config import module_map
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class Analyzer():

    def __init__(self, text):
        self.text = text
        self.words = self.tokenize_text()
        self._preprocessed_text = None
        self._preprocessed_words = None
        self.modules = []
        self.analysis = {}


    def get_sentences(self) -> list:
        text = self.get_text()
        sentence_list = nltk.sent_tokenize(text)
        sentence_dict_list = [{'id': i, 'content': sentence} for i, sentence in enumerate(sentence_list, 1)]
        return sentence_dict_list


    def tokenize_text(self) -> list:
        text = self.get_text()
        sentences = self.get_sentences()
        tokens = [word for sentence in sentences for word in nltk.word_tokenize(sentence['content']) if word.isalpha()]
        return tokens

    
    @property
    def preprocessed_text(self):
        if self._preprocessed_text is None:
            self._preprocessed_text = self.preprocess_text(
                remove_stopwords=True, lemmatization=True
            )
        return self._preprocessed_text

    @property
    def preprocessed_words(self):
        if self._preprocessed_words is None:
            self._preprocessed_words = nltk.word_tokenize(
                self.preprocessed_text
            )
        return self._preprocessed_words

    
    def preprocess_text(self, remove_stopwords=False, stemming=False, lemmatization=False) -> str:
        text = self.get_text().lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

        if remove_stopwords:
            STOPWORDS = set(stopwords.words('english'))
            text = " ".join([word for word in str(text).split() if word not in STOPWORDS])

        if stemming:
            stemmer = PorterStemmer()
            text = " ".join([stemmer.stem(word) for word in text.split()])

        if lemmatization:
            lemmatizer = WordNetLemmatizer()
            text = " ".join([lemmatizer.lemmatize(word) for word in text.split()])

        return text


    def tokenize_preprocessed_text(self) -> list:
        preprocessed_text = self.get_preprocessed_text()
        preprocessed_words = nltk.word_tokenize(preprocessed_text)
        return preprocessed_words


    def get_text(self):
        text = self.text
        return text


    def get_words(self) -> list:
        return self.words


    def get_preprocessed_text(self) -> str:
        preprocessed_text = self.preprocessed_text
        return preprocessed_text


    def get_preprocessed_words(self) -> list:
        return self.preprocessed_words


    def plug_modules(self, focus):
        if "text" in focus:
            text_module = TextModule(self)
            text_module.plug()
        if 'word' in focus:
            word_module = WordModule(self)
            word_module.plug()
        if 'read' in focus:
            readability_module = ReadabilityModule(self)
            readability_module.plug()
        if 'sentiment' in focus:
            sentiment_module = SentimentModule(self)
            sentiment_module.plug()


    def generate_analysis(self) -> dict:
        for module in self.modules:
            self.analysis[module.name] = module.analyze()
        return self.analysis