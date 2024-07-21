import json
from tabulate import tabulate


class ReportGenerator:
    def __init__(self, analysis):
        self.analysis = analysis
    def save_report(self, filename):
        pass


class JSONReportGenerator(ReportGenerator):
    def __init__(self, analysis):
        super().__init__(analysis)
    def save_report(self, filename):
        with open(filename, "w") as jsonfile:
            json.dump(self.analysis, jsonfile, indent=4)


class TXTReportGenerator(ReportGenerator):
    def __init__(self, analysis):
        super().__init__(analysis)
    def save_report(self, filename):
        with open(filename, "w") as txtfile:
            txtfile.write("\nTEXT STATISTICS:\n")
            txtfile.write(''.join(map(lambda item: f"- {item[0].replace('_', ' ').title()}: {item[1]}\n", self.analysis['text_statistics'].items())))
            txtfile.write("\n---\n")

            if 'word_analysis' in self.analysis:
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
                txtfile.write("\n---\n")

            if 'readibility_analysis' in self.analysis:
                txtfile.write("\nReadibility Details:\n")
                txtfile.write(''.join(map(lambda item: f"- {item[0].replace('_', ' ').title()}: {item[1]}\n", self.analysis['readibility_analysis'].items())))
                txtfile.write("\n---\n")

            if 'ngram_analysis' in self.analysis:
                txtfile.write("\nN-grams:\n")
                txtfile.write(*map(lambda item: f"- {item[0]}: {item[1]}\n", self.analysis['ngram_analysis'].items()))
                txtfile.write("\n---\n")

            if 'ner_analysis' in self.analysis:
                txtfile.write("\nNamed entities:\n")
                txtfile.write(*map(lambda item: f"- {item[1]} ({item[0]})\n", self.analysis['ner_analysis']))
                txtfile.write("\n---\n")
            
            if 'sentiment_analysis' in self.analysis:
                txtfile.write("\nSentiment:\n")
                txtfile.write(''.join(map(lambda item: f"\n{item['sentence']}\n    - Negative: {item['neg']}\n    - Neutral: {item['neu']}\n    - Positive: {item['pos']}\n    - Compound: {item['compound']}\n", self.analysis['sentiment_analysis'])))
                txtfile.write("\n---\n")

    # JSON-LD
    # TURTLE
    # HTML-RDFa
