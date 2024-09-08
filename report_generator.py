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
            txtfile.write(f"# LODOT REPORT FOR {filename}")
            txtfile.write("\n## TEXT STATISTICS\n")
            txtfile.write(''.join(map(lambda item: f"- **{item[0].replace('_', ' ').title()}**: {item[1]}\n", self.analysis['text_statistics'].items())))

            if 'text_composition' in self.analysis:
                txtfile.write("\n## TEXT COMPOSITION\n")
                txtfile.write(''.join(map(lambda item: f"- **{item[0].replace('_', ' ').title()}**: {item[1]}\n", self.analysis['text_composition'].items())))

            if 'readability_analysis' in self.analysis:
                txtfile.write("\n## READABILITY\n")
                txtfile.write(''.join(map(lambda item: f"- **{item[0].replace('_', ' ').title()}**: {item[1]}\n", self.analysis['readability_analysis'].items())))
            
            if 'sentiment_analysis' in self.analysis:
                txtfile.write("\n## SENTIMENT ANALYSIS\n")
                txtfile.write(''.join(map(lambda item: f"- {item[0]}: {item[1]}\n", self.analysis['sentiment_analysis'].items())))
                #txtfile.write(f"\n- Negative: {self.analysis['sentiment_analysis']['neg']}\n- Neutral: {self.analysis['sentiment_analysis']['neu']}\n- Positive: {self.analysis['sentiment_analysis']['pos']}\n- Compound: {self.analysis['sentiment_analysis']['compound']}\n")

    # JSON-LD
    # TURTLE
    # HTML-RDFa
