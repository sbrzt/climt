# src/modules/readability_module.py

import textstat
from src.modules.analysis_module import AnalysisModule


class ReadabilityModule(AnalysisModule):
    
    def __init__(self, analyzer):
        super().__init__(analyzer, "readability")
        self.text = analyzer.get_text()

    def analyze(self) -> dict:
        readability_stats = {
            "flesch_reading_ease": round(textstat.flesch_reading_ease(self.text), 2),
            "flesch_kincaid_grade": round(textstat.flesch_kincaid_grade(self.text), 2),
            "gunning_fog": textstat.gunning_fog(self.text),
            "smog_index": textstat.smog_index(self.text),
            "automated_readability_index": round(textstat.automated_readability_index(self.text), 2),
            "coleman_liau_index": round(textstat.coleman_liau_index(self.text), 2),
        }
        return readability_stats