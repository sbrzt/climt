from modules.analysis_module import AnalysisModule
from nltk.sentiment import SentimentIntensityAnalyzer


class SentimentModule(AnalysisModule):

    def __init__(self, analyzer):
        super().__init__(analyzer)

    def get_polarity_scores(self, sentiment_intensity_analyzer, text):
        '''
        '''
        polarity_scores = sentiment_intensity_analyzer.polarity_scores(text)
        return polarity_scores
    

    def analyze(self):
        '''
        Return a detailed analysis for the sentiment polarities... 

        Output:
            - a dictionary representing the sentiment analysis...
        
        FW:
        - tone
        - personalism
        '''
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