# src/modules/pos.py

from collections import Counter
from src.modules.analysis import AnalysisModule


class POSModule(AnalysisModule):
    
    def __init__(self, analyzer):
        super().__init__(analyzer, "pos")
        self.doc = analyzer.doc

    def analyze(self) -> dict:
        pos_counts = Counter([token.pos_ for token in self.doc if token.is_alpha])
        total = sum(pos_counts.values())
        pos_stats = {
            pos: {
                "count": count,
                "freq": round(count / total * 100, 2)
            }
            for pos, count in pos_counts.items()
        }
        return pos_stats