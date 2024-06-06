import nltk, statistics, string
from collections import Counter
from nltk.corpus import stopwords

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
    
    # Character count
    char_count = len(text)

    # Word count
    word_count = len(words)

    # Top 50 words
    word_freq = Counter(words).most_common(50)

    pos_tags = dict(nltk.pos_tag(words))

    # Calculate frequency in terms of percent and get POS tags
    word_details = []
    for word, count in word_freq:
        frequency_percent = (count / word_count) * 100
        pos_tag = pos_tags.get(word, 'N/A')
        word_details.append({
            'word': word,
            'occurrences': count,
            'frequency_percent': frequency_percent,
            'pos_tag': pos_tag
        })

    analysis = {
        'char_count': char_count,
        'word_count': word_count,
        'word_details': word_details
    }

    return analysis