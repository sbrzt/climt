import pytest
from src.analyzer import Analyzer
from src.modules.sentiment_module import SentimentModule


sample_text = "Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness."

analyzer = Analyzer(sample_text)
sentiment_module = SentimentModule(analyzer)


def test_analyze():
    result = sentiment_module.analyze()

    assert -1 <= result["overall"]["polarity"] <= 1
    assert 0 <= result["overall"]["subjectivity"] <= 1

    sentences = result["sentences"]

    for _, data in sentences.items():
        assert -1 <= data["polarity"] <= 1
        assert 0 <= data["subjectivity"] <= 1
        