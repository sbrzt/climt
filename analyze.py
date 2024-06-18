import nltk, statistics, string, convert, produce
from collections import Counter
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
import pprint

# Ensure required NLTK resources are downloaded
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')
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

def analyze_text(text):
    # Tokenize text into words and sentences
    words = preprocess_text(text)
    
    # COUNTS
    char_count = len(text)
    word_count = len(words)

    # LEMMA
    lemmatizer = nltk.WordNetLemmatizer()

    # WORD
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
            'pos_tag': wordnet_pos,
            'lemma': lemma,
            'senses': senses
        })

    analysis = {
        'char_count': char_count,
        'word_count': word_count,
        'word_details': word_details
    }

    return analysis
    