# src/analyzer.py

import spacy
from spacy.cli import download
import string
from config import MODULE_MAP


def load_spacy_model(name="en_core_web_sm"):
    try:
        return spacy.load(name)
    except OSError:
        print(f"Downloading spaCy model '{name}'...")
        download(name)
        return spacy.load(name)


class Analyzer():

    def __init__(self, text):
        self.text = text
        self.nlp = load_spacy_model()
        self.doc = self.nlp(text)
        self.words = self.tokenize_text()
        self._preprocessed_text = None
        self._preprocessed_words = None
        self.modules = []
        self.analysis = {}

    def get_text(self) -> str:
        return self.text

    def get_words(self) -> list:
        return self.words

    def get_sentences(self) -> list:
        return [sent.text.strip() for sent in self.doc.sents]

    def tokenize_text(self) -> list:
        return [token.text for token in self.doc if token.is_alpha]

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
            self._preprocessed_words = self.preprocessed_text.split()
        return self._preprocessed_words

    def preprocess_text(
        self, 
        remove_stopwords=False, 
        stemming=False, 
        lemmatization=False) -> str:
        tokens = []
        for token in self.doc:
            if not token.is_alpha:
                continue
            if remove_stopwords and token.is_stop:
                continue
            if lemmatization:
                tokens.append(token.lemma_.lower())
            else:
                tokens.append(token.text.lower())
        return " ".join(tokens)

    def plug_modules(self, focus):
        for f in focus:
            if f in MODULE_MAP:
                module = MODULE_MAP[f](self)
                module.plug()

    def generate_analysis(self):
        for module in self.modules:
            self.analysis[module.name] = module.analyze()
        return self.analysis