from modules.analysis_module import AnalysisModule
from nltk.sentiment import SentimentIntensityAnalyzer


class SentimentModule(AnalysisModule):
    """
    A module for performing sentiment analysis on a text, specifically analyzing the sentiment 
    of each paragraph. The module uses the SentimentIntensityAnalyzer from the VADER library 
    to compute polarity scores and classify the sentiment as positive, negative, or neutral.

    Inherits:
        AnalysisModule: The base class for all analysis modules.

    Attributes:
        analyzer (TextAnalyzer): An instance of the TextAnalyzer class that provides access 
                                 to the text data and related analysis methods.
    """

    def __init__(self, analyzer):
        """
        Initializes the SentimentModule with a reference to the analyzer.

        Args:
            analyzer (TextAnalyzer): The text analyzer instance containing the text and 
                                     methods for analysis.
        """
        super().__init__(analyzer)

    def get_polarity_scores(self, sentiment_intensity_analyzer, text):
        """
        Computes the polarity scores for the given text using the provided sentiment analyzer.

        Args:
            sentiment_intensity_analyzer (SentimentIntensityAnalyzer): An instance of VADER's 
                                                                       SentimentIntensityAnalyzer.
            text (str): The text (or paragraph) for which to compute the polarity scores.

        Returns:
            dict: A dictionary containing polarity scores, which include 'neg' (negative), 
                  'neu' (neutral), 'pos' (positive), and 'compound' (overall sentiment score).
        """
        polarity_scores = sentiment_intensity_analyzer.polarity_scores(text)
        return polarity_scores
    

    def analyze(self):
        """
        Analyzes the sentiment of each paragraph in the text and classifies it as positive, 
        negative, or neutral based on the compound polarity score.

        The compound score is interpreted as follows:
        - Positive if compound score > 0.05
        - Negative if compound score < -0.05
        - Neutral if -0.05 <= compound score <= 0.05

        Returns:
            dict: A dictionary where each key is a paragraph ID and the value is another 
                  dictionary containing the polarity scores and the sentiment label (positive, 
                  negative, or neutral) for that paragraph.
        """
        sia = SentimentIntensityAnalyzer()
        polarity_scores = {}
        paragraphs = self.analyzer.get_paragraphs()
        for paragraph in paragraphs:
            paragraph_polarity_scores = self.get_polarity_scores(sia, paragraph['content'])
            compound_score = paragraph_polarity_scores['compound']
            polarity_scores[paragraph['id']] = {
                'paragraph_id': paragraph['id'],
                'polarity_scores': paragraph_polarity_scores,
                'label': 'positive' if compound_score > 0.05 else 'negative' if compound_score < -0.05 else 'neutral'
            }
        return polarity_scores