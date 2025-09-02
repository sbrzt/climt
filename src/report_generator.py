# report_generator.py

import json


class ReportGenerator:
    """
    Base class for generating reports from text analysis. This class provides a generic
    interface for saving reports in different formats, such as JSON or plain text.

    Attributes:
        analysis (dict): A dictionary containing the results of text analysis.
    """

    def __init__(self, analysis):
        """
        Initializes the ReportGenerator with the analysis data.

        Args:
            analysis (dict): The results of the text analysis to be included in the report.
        """
        self.analysis = analysis

    def save_report(self, filename):
        """
        Saves the analysis report to the specified file. This method should be 
        implemented by subclasses to handle different report formats.

        Args:
            filename (str): The name of the file where the report will be saved.
        """
        pass


class TXTReportGenerator(ReportGenerator):
    """
    A subclass of ReportGenerator that saves the analysis report in plain text format.

    The report includes sections such as text statistics, text composition, word analysis, 
    readability, and sentiment analysis, if available.

    Inherits:
        ReportGenerator: Base class for report generation.
    """

    def __init__(self, analysis):
        """
        Initializes the TXTReportGenerator with the analysis data.

        Args:
            analysis (dict): The results of the text analysis to be included in the report.
        """
        super().__init__(analysis)

    def save_report(self, filename):
        """
        Saves the analysis report in plain text format. The report is organized into sections, 
        each containing relevant metrics such as text statistics, word analysis, readability, 
        and sentiment analysis.

        Args:
            filename (str): The name of the file where the report will be saved.
        """
        with open(filename, "w") as txtfile:
            txtfile.write(f"# LODOT REPORT FOR {filename}")
            txtfile.write("\n## TEXT STATISTICS\n")
            txtfile.write(''.join(map(lambda item: f"- **{item[0].replace('_', ' ').title()}**: {item[1]}\n", self.analysis['text_statistics'].items())))

            if 'text_composition' in self.analysis:
                txtfile.write("\n## TEXT COMPOSITION\n")
                txtfile.write(''.join(map(lambda item: f"- **{item[0].replace('_', ' ').title()}**: {item[1]}\n", self.analysis['text_composition'].items())))

            if 'word_analysis' in self.analysis:
                txtfile.write('\n## WORD ANALYSIS\n')
                txtfile.write(''.join(map(lambda item: f"- **{item[0].replace('_', ' ').title()}**: {item[1]}\n", self.analysis['word_analysis'].items())))

            if 'readability_analysis' in self.analysis:
                txtfile.write("\n## READABILITY\n")
                txtfile.write(''.join(map(lambda item: f"- **{item[0].replace('_', ' ').title()}**: {item[1]}\n", self.analysis['readability_analysis'].items())))
            
            if 'sentiment_analysis' in self.analysis:
                txtfile.write("\n## SENTIMENT ANALYSIS\n")
                txtfile.write(''.join(map(lambda item: f"- {item[0]}: {item[1]}\n", self.analysis['sentiment_analysis'].items())))

    # JSON-LD
    # TURTLE
    # HTML-RDFa
