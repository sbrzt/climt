import json
from tabulate import tabulate

class ReportGenerator:
    def __init__(self, analysis):
        self.analysis = analysis

    # JSON
    def save_json(self, filename):
        with open(filename, "w") as jsonfile:
            json.dump(self.analysis, jsonfile, indent=4)

    # TXT
    def save_txt(self, filename):
        with open(filename, "w") as txtfile:
            txtfile.write(f"Character Count: {self.analysis['char_count']}\n")
            txtfile.write(f"Word Count: {self.analysis['word_count']}\n")
            txtfile.write(f"Sentence Count: {self.analysis['sentence_count']}\n")
            txtfile.write(f"Flesch Kincaid Score: {self.analysis['flesch_kincaid_score']:.2f}\n")

            if 'word_details' in self.analysis:
                txtfile.write("\nWord Details:\n")
                txtfile.write(tabulate([
                    [
                        detail['word'],
                        detail['occurrences'],
                        f"{detail['frequency_percent']:.2f}",
                        detail['pos_tag'],
                        detail['lemma'],
                        ", ".join(detail['senses'])
                    ] for detail in self.analysis['word_details']
                ], headers=["Word", "Occurrences", "Frequency (%)", "POS Tag", "Lemma", "Senses"]))
    
    # JSON-LD
    # TURTLE
    # HTML-RDFa
