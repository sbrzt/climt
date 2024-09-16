from src.modules.analysis_module import AnalysisModule
import textstat


class ReadabilityModule(AnalysisModule):
    """
    A module for calculating various readability scores for a given text. The module uses 
    multiple readability formulas to provide insights into the text's complexity and estimated 
    reading and speaking times.

    Inherits:
        AnalysisModule: The base class for all analysis modules.

    Attributes:
        analyzer (TextAnalyzer): An instance of the TextAnalyzer class that provides access 
                                 to the text data and related analysis methods.
    """

    def __init__(self, analyzer):
        """
        Initializes the ReadabilityModule with a reference to the analyzer.

        Args:
            analyzer (TextAnalyzer): The text analyzer instance containing the text and 
                                     methods for analysis.
        """
        super().__init__(analyzer)

    def analyze(self):
        """
        Performs readability analysis on the text using multiple readability metrics.

        The analysis includes:
        - Flesch Reading Ease
        - SMOG Index
        - Flesch-Kincaid Grade Level
        - Coleman-Liau Index
        - Automated Readability Index
        - Dale-Chall Readability Score
        - Difficult Words Count
        - Linsear Write Formula
        - Gunning Fog Index
        - Text Standard (estimated grade level)
        - Estimated Reading Time
        - Estimated Speaking Time

        Returns:
            dict: A dictionary containing the calculated readability scores and estimated times 
                  for reading and speaking the text.
        """
        text = self.analyzer.get_text()
        word_count = self.analyzer.get_word_count()
        readability_scores = {
            'flesch_reading_ease': textstat.flesch_reading_ease(text),
            'smog_index': textstat.smog_index(text),
            'flesch_kincaid_grade': textstat.flesch_kincaid_grade(text),
            'coleman_liau_index': textstat.coleman_liau_index(text),
            'automated_readability_index': textstat.automated_readability_index(text),
            'dale_chall_readability_score': textstat.dale_chall_readability_score(text),
            'difficult_words': textstat.difficult_words(text),
            'linsear_write_formula': textstat.linsear_write_formula(text),
            'gunning_fog': textstat.gunning_fog(text),
            'text_standard': textstat.text_standard(text),
            'reading_time': f'{word_count / 225} min.',
            'speaking_time': f'{word_count / 125} min.'
        }
        return readability_scores