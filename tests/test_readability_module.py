import pytest
from src.analyzer import Analyzer
from src.modules.readability_module import ReadabilityModule


sample_text = "Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness."

analyzer = Analyzer(sample_text)
readability_module = ReadabilityModule(analyzer)


def test_analyze():
    result = readability_module.analyze()
    assert 0 <= result["flesch_reading_ease"] <= 120
    assert 0 <= result["flesch_kincaid_grade"] <= 20
    assert 0 <= result["gunning_fog"] <= 20
    assert 0 <= result["smog_index"] <= 20
    assert 0 <= result["automated_readability_index"] <= 20
    assert 0 <= result["coleman_liau_index"] <= 20