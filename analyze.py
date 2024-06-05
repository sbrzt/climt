import nltk, statistics

def analyze_text(text):
    # Tokenize text into words and sentences
    words = nltk.word_tokenize(text)
    sentences = nltk.sent_tokenize(text)
    
    # Character count
    char_count = len(text)
    
    # Word count
    word_count = len(words)
    
    # Sentence count
    sentence_count = len(sentences)

    # Average length of words
    avg_word_length = statistics.mean(len(word) for word in words) if words else 0


    analysis = {
        'char_count': char_count,
        'word_count': word_count,
        'sentence_count': sentence_count,
        'average_word_length': avg_word_length
    }

    return analysis