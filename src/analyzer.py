import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class Analyzer():
    """
    """

    def __init__(self, text):
        """
        """
        self.text = text
        self.words = self.tokenize_text()
        self.preprocessed_text = self.preprocess_text(remove_stopwords=True, lemmatization=True)
        self.preprocessed_words = self.tokenize_preprocessed_text()
        self.modules = []
        self.analysis = {}


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


    def tokenize_preprocessed_text(self) -> list:
        """
        Tokenizes the preprocessed text into words.

        Returns:
            list: A list of preprocessed words.
        """
        preprocessed_text = self.get_preprocessed_text()
        preprocessed_words = nltk.word_tokenize(preprocessed_text)
        return preprocessed_words


    def get_text(self):
        text = self.text
        return text


    def get_words(self) -> list:
        """
        Returns the tokenized words of the original text.

        Returns:
            list: A list of words.
        """
        words = self.words
        return words


    def get_preprocessed_text(self) -> str:
        preprocessed_text = self.preprocessed_text
        return preprocessed_text


    def get_preprocessed_words(self) -> list:
        """
        Returns the tokenized words from the preprocessed text.

        Returns:
            list: A list of preprocessed words.
        """
        preprocessed_words = self.preprocessed_words
        return preprocessed_words


    def plug_modules(self, focus):
        if "text" in focus:
            text_module = TextModule(self)
            text_module.plug()


    def generate_analysis(self):
        for module in self.modules:
            self.analysis[module.name] = module.analyze()
        return self.analysis