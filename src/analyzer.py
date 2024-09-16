


class Analyzer():
    """
    """

    def __init__(self, text):
        """
        """
        self.text = text
        self.modules = []
        self.analysis = {}


    def plug_modules(self, focus):
        if "text" in focus:
            text_module = TextModule(self)
            text_module.plug()
        if 'word' in focus:
            word_module = WordModule(self)
            word_module.plug()
        if 'read' in focus:
            readability_module = ReadabilityModule(self)
            readability_module.plug()
        if 'sentiment' in focus:
            sentiment_module = SentimentModule(self)
            sentiment_module.plug()


    def generate_analysis(self):
        for module in self.modules:
            self.analysis[module.name] = module.analyze()
        return self.analysis