# modules/analysis.py


class AnalysisModule():

    def __init__(self, analyzer, name=None):
        self.name = name
        self.analyzer = analyzer
    
    def plug(self):
        self.analyzer.modules.append(self)

    def analyze(self):
        pass