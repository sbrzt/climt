import pytest
from src.analyzer import Analyzer
from src.modules.pos_module import POSModule


sample_text = "Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness."

analyzer = Analyzer(sample_text)
pos_module = POSModule(analyzer)

def test_analyze():
    result = pos_module.analyze()

    assert any(tag in result for tag in ["NOUN", "PROPN"])
    assert "VERB" in result or "AUX" in result
    assert "ADJ" in result

    total_freq = sum(stats["freq"] for stats in result.values())
    assert pytest.approx(total_freq, rel=1e-2) == 100.0