# modules/words.py

import math
import matplotlib.pyplot as plt
from collections import Counter
from src.modules.analysis import AnalysisModule
from src.utils.visualization import (
    print_table,
    print_plot,
    save_plot
)


class WordsModule(AnalysisModule):

    def __init__(self, analyzer, top_n=20):
        super().__init__(analyzer, "words")
        self.words = [w.lower() for w in analyzer.get_words() if w.isalpha()]
        self.top_n = top_n
        self.word_counts = Counter(self.words)
        self.total_words = len(self.words)
        self.word_freq = [(word, count, round(count / self.total_words * 100, 2)) for word, count in self.word_counts.most_common(self.top_n)]

    def analyze(self) -> dict:
        word_stats = {
            word: {
                "count": count, 
                "freq": freq
            } for word, count, freq in self.word_freq
        }
        return word_stats

    def print_table(self):
        print_table(self.word_freq, headers=("Word", "Count", "Freq"))

    def print_plot(self):
        print_plot(self.word_freq)

    def save_plot(
        self, 
        filename="word_freq.png",
        title="Top Word Frequencies"
        ):
        save_plot(self.word_freq, filename=filename, title=title)
