from src.modules.analysis_module import AnalysisModule
from nltk.corpus import wordnet as wn


class WordModule(AnalysisModule):
    """
    A module for performing detailed word analysis on the text. This module analyzes word 
    frequencies, part-of-speech (POS) tags, and semantic senses for the most common words 
    in the text using WordNet.

    Inherits:
        AnalysisModule: The base class for all analysis modules.

    Attributes:
        analyzer (TextAnalyzer): An instance of the TextAnalyzer class that provides access 
                                 to the text data and related analysis methods.
    """

    def __init__(self, analyzer):
        """
        Initializes the WordModule with a reference to the analyzer.

        Args:
            analyzer (TextAnalyzer): The text analyzer instance containing the text and 
                                     methods for analysis.
        """
        super().__init__(analyzer)

    def analyze(self):
        """
        """
        word_details = {}
        word_frequencies = self.analyzer.get_most_common_word_frequencies()
        for word, count in word_frequencies:
            frequency_percent = (count / self.analyzer.get_word_count()) * 100
            pos_tag = dict(self.analyzer.get_word_pos()).get(word, 'N/A')
            synsets = wn.synsets(word, pos=self.analyzer.get_wordnet_pos(pos_tag))
            senses = [synset.definition() for synset in synsets]
            word_details[word] = {
                'occurrences': count,
                'frequency_percent': frequency_percent,
                'pos_tag': pos_tag,
                'senses': senses
            }
        return word_details