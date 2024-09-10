from modules.analysis_module import AnalysisModule

class WordModule(AnalysisModule):

    def __init__(self, analyzer):
        super().__init__(analyzer)
    
    def most_common_word_frequencies(self):
        pass

    def analyze(self):
        word_details = []
        for word, count in self.most_common_word_frequencies():
            frequency_percent = (count / self.__word_count) * 100
            pos_tag = dict(self.__word_pos).get(word, 'N/A')
            synsets = wn.synsets(word, pos=self.__get_wordnet_pos(pos_tag))
            senses = [synset.definition() for synset in synsets]
            word_details.append({
                'word': word,
                'occurrences': count,
                'frequency_percent': frequency_percent,
                'pos_tag': pos_tag,
                'senses': senses
            })
        return word_details