# src/modules/sentiment.py

from textblob import TextBlob
from src.modules.analysis import AnalysisModule


class SentimentModule(AnalysisModule):

    def __init__(self, analyzer):
        super().__init__(analyzer, "sent")
        self.text = analyzer.get_text()
        self.sentences = analyzer.get_sentences()

    def analyze(self) -> dict:
        overall = TextBlob(self.text).sentiment
        sentence_sentiments = {}
        for i, sentence in enumerate(self.sentences, start=1):
            detail = TextBlob(str(sentence)).sentiment
            sentence_sentiments[i] = {
                "content": str(sentence),
                "polarity": round(detail.polarity, 3),
                "subjectivity": round(detail.subjectivity, 3)
            }
        return {
            "overall": {
                "polarity": round(overall.polarity, 3),
                "subjectivity": round(overall.subjectivity, 3)
            },
            "sentences": sentence_sentiments
        }
