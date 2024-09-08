from modules.analysis_module import AnalysisModule
from collections import Counter


class CompositionModule(AnalysisModule):
    
    def __init__(self, analyzer):
        super().__init__(analyzer)

    def analyze(self):
        '''
        Return a detailed analysis of the composition of the text...

        Output:
            - a dictionary...
        '''
        counts = Counter(tag for word, tag in self.analyzer.get_word_pos())
        adjective_count = counts['JJ']
        adverb_count = counts['RB'] + counts['RBR'] + counts['RBS'] + counts['WRB']
        conjunction_count = counts['CC'] + counts['IN']
        determiner_count = counts['DT']
        noun_count = counts['NN'] + counts['NNS']
        proper_noun_count = counts['NNP'] + counts['NNPS']
        preposition_count = counts['IN'] + counts['PP']
        pronoun_count = counts['PRP'] + counts['PRP$'] + counts['WP'] + counts['WP$']
        verb_count = counts['VBD'] + counts['VBG'] + counts['VBN'] + counts['VBP'] + counts['VBZ'] + counts['VP']
        text_composition_analysis = {
            'adjectives': adjective_count,
            'adverbs': adverb_count,
            'conjunctions': conjunction_count,
            'determiners': determiner_count,
            'nouns': noun_count,
            'proper_nouns': proper_noun_count,
            'prepositions': preposition_count,
            'pronouns': pronoun_count,
            'verbs': verb_count
        }        
        return text_composition_analysis