# main.py

import argparse
import pprint
from src.analyzer import Analyzer
from src.report_generator import *


def main():
    parser = argparse.ArgumentParser(
        description="Analyze a text and generate reports in various formats."
    )
    parser.add_argument(
        "input", 
        nargs='?', 
        help="Raw text"
    )
    parser.add_argument(
        "--file", 
        help="Path to the input text file"
    )
    parser.add_argument(
        "--output", 
        choices=[
            "stream",
            "txt",
            "md",
        ], 
        default="stream", 
        help="Output format"
    )
    parser.add_argument(
        "--outfile", 
        help="Output file name"
    )
    parser.add_argument(
        "--focus", 
        nargs='*', 
        choices=[
            "text",
            "word_stats",
            "pos_stats"
        ], 
        default=["text"], 
        help="Focus of the analysis"
    )

    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as f:
            text = f.read()
    elif args.input:
        text = args.input
    else:
        raise Exception("No input text or file provided.")
        
    analyzer = Analyzer(text)
    analyzer.plug_modules(args.focus)
    analyzer.generate_analysis()
    analysis = analyzer.analysis

    if args.output == "stream":
        pprint.pprint(analysis)
    else:
        if not args.outfile:
            print(f"Filename required for .{args.output} output")
        else:
            if args.output == "txt" or args.output == "md":
                report_generator = TXTReportGenerator(analysis)
            else:
                print("Invalid format choice")
    
        report_generator.save_report(f"{args.outfile}.{args.output}")

if __name__ == "__main__":
    main()
