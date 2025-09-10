# modules/text.py

from modules.analysis import AnalysisModule


class TextModule(AnalysisModule):
    
    def __init__(self, analyzer):
        super().__init__(analyzer, "text")
        self._text = self.analyzer.get_text()
        self._sentences = self.analyzer.get_sentences()
        self._words = self.analyzer.get_words()
        self._paragraphs = self.get_paragraphs()


    def get_character_count(self) -> int:
        return len(self._text)

    def get_word_count(self) -> int:
        return len(self._words)

    def get_character_per_word(self) -> int:
        return round(len(self._text) / len(self._words), 2)

    def get_paragraphs(self) -> list:
        return [p for p in self._text.split("\n") if p.strip()]

    def get_paragraph_count(self) -> int:
        return len(self._paragraphs)

    def get_sentence_count(self) -> int:
        return len(self._sentences)

    def get_word_count_per_sentence(self) -> float:
        return len(self._words) / len(self._sentences)

    def get_word_count_per_paragraph(self) -> float:
        return len(self._words) / len(self._paragraphs)

    def get_sentence_count_per_paragraph(self) -> float:
        return len(self._sentences) / len(self._paragraphs)

    def get_unique_word_count(self) -> int:
        return len(set(self._words))

    def analyze(self) -> dict:
        text_stats = {
            'character_count': self.get_character_count(),
            'character_per_word': self.get_character_per_word(),
            'word_count': self.get_word_count(),
            'paragraph_count': self.get_paragraph_count(),
            'words_per_paragraph': self.get_word_count_per_paragraph(),
            'sentences_per_paragraph': self.get_sentence_count_per_paragraph(),
            'sentence_count': self.get_sentence_count(),
            'words_per_sentence': self.get_word_count_per_sentence(),
            'unique_word_count': self.get_unique_word_count(),
        }
        return text_stats

