import pytest
from src.analyzer import Analyzer
from src.modules.word_stats_module import WordStatModule


sample_text = "Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness."

analyzer = Analyzer(sample_text)
word_stats_module = WordStatModule(analyzer)

def test_analyze():
    result = word_stats_module.analyze()
    assert "blessed" in result
    assert "charity" in result
    assert result["blessed"]["count"] == 1
    assert result["charity"]["count"] == 1
    assert result["blessed"]["freq"] == pytest.approx(100 / 21, rel=1e-2)
    assert result["charity"]["freq"] == pytest.approx(100 / 21, rel=1e-2)
