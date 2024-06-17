import nltk, statistics, string
from collections import Counter
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
import pprint

#nltk.download('wordnet')

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize text into words
    words = nltk.word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    return words

def analyze_text(text):
    # Tokenize text into words and sentences
    words = preprocess_text(text)
    
    # CHARACTER
    '''
    char_count = len(text)
    char_freq = Counter(text.lower()).most_common()
    char_details = []
    for char, count in char_freq:
        frequency_percent = (count / char_count) * 100
        char_details.append({
            'char': char,
            'occurrences': count,
            'frequency_percent': frequency_percent,
        })
    '''

    lemmatizer = nltk.WordNetLemmatizer()

    def get_wordnet_pos(tag):
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

    # WORD
    word_count = len(words)
    word_freq = Counter(words).most_common(50)
    pos_tags = dict(nltk.pos_tag(words))
    word_details = []
    for word, count in word_freq:
        frequency_percent = (count / word_count) * 100
        pos_tag = pos_tags.get(word, 'N/A')
        wordnet_pos = get_wordnet_pos(pos_tag) or wn.NOUN
        lemma = lemmatizer.lemmatize(word, pos=wordnet_pos)
        synsets = wn.synsets(word, pos=wordnet_pos)
        senses = [synset.definition() for synset in synsets]
        word_details.append({
            'word': word,
            'occurrences': count,
            'frequency_percent': frequency_percent,
            'pos_tag': pos_tag,
            'lemma': lemma,
            'senses': senses
        })



    analysis = {
        #'char_count': char_count,
        #'char_details': char_details,
        'word_count': word_count,
        'word_details': word_details
    }

    pprint.pprint(analysis)