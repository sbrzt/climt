# modules/word_stats_module.py

import math
import matplotlib.pyplot as plt
from collections import Counter
from src.modules.analysis_module import AnalysisModule


class WordStatModule(AnalysisModule):

    def __init__(self, analyzer, top_n=20):
        super().__init__(analyzer, "word_stats")
        self.words = [w.lower() for w in analyzer.get_words() if w.isalpha()]
        self.top_n = top_n
        self.word_counts = Counter(self.words)
        self.total_words = len(self.words)
        self.word_freq = [(word, count, count / self.total_words * 100) for word, count in self.word_counts.most_common(self.top_n)]

    def print_table(self):
        print(f"{'Word':<10}{'Count':<10}{'Freq':<10}")
        for word, count, freq in self.word_freq:
            print(f"{word:<10}{count:<10}{freq:<10.4f}")
    
    def print_histogram(self, max_width=60, symbol="#"):
        max_count = max([count for word, count, freq in self.word_freq])
        for word, count, freq in self.word_freq:
            bar = symbol * int(count / max_count * max_width)
            print(f"{word:<10}{bar}")

    def save_plot(self, filename="word_freq.png"):
        words = [word for word, count, freq in self.word_freq]
        counts = [count for word, count, freq in self.word_freq]
        plt.figure(figsize=(10,6))
        plt.bar(words, counts, color="skyblue")
        plt.xticks(rotation=45)
        plt.ylabel("Count")
        plt.title("Top Word Frequencies")
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()

    def analyze(self):
        word_stats_analysis = {
            word: {
                "count": count, 
                "freq": freq
            } for word, count, freq in self.word_freq
        }
        return word_stats_analysis
