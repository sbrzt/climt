from modules.analysis_module import AnalysisModule
import textstat


class ReadabilityModule(AnalysisModule):

    def __init__(self, analyzer):
        super().__init__(analyzer)

    def analyze(self):
        '''
        Return a detailed analysis for the readibility of the text in terms of scores, each based on a specific metric (e.g. Flesch-Kincaid Grade, Automated Readibility Index, etc.)
        
        Output:
            - a dictionary representing the readibility analysis

        FW:
        - sentences > 30 syllables
        - words > 12 letters
        - adverb count < 4%
        - passive voice count
        '''
        text = self.analyzer.get_text()
        word_count = self.analyzer.get_word_count()
        readability_scores = {
            'flesch_reading_ease': textstat.flesch_reading_ease(text),
            'smog_index': textstat.smog_index(text),
            'flesch_kincaid_grade': textstat.flesch_kincaid_grade(text),
            'coleman_liau_index': textstat.coleman_liau_index(text),
            'automated_readability_index': textstat.automated_readability_index(text),
            'dale_chall_readability_score': textstat.dale_chall_readability_score(text),
            'difficult_words': textstat.difficult_words(text),
            'linsear_write_formula': textstat.linsear_write_formula(text),
            'gunning_fog': textstat.gunning_fog(text),
            'text_standard': textstat.text_standard(text),
            'reading_time': f'{word_count / 225} min.',
            'speaking_time': f'{word_count / 125} min.'
        }
        return readability_scores