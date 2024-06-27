import argparse
import pprint
from text_analyzer import TextAnalyzer
from report_generator import ReportGenerator

def main():
    parser = argparse.ArgumentParser(
        description="Analyze a text and generate reports in various formats."
    )
    parser.add_argument(
        "input", 
        nargs='?', 
        help="Raw text or path to the input text file"
    )
    parser.add_argument(
        "--file", 
        help="Path to the input text file"
    )
    parser.add_argument(
        "--output", 
        choices=[
            "stream", 
            "json", 
            "txt"
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
        choices=["word"], 
        default=["word"], 
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
        
    analyzer = TextAnalyzer(text)
    analysis = analyzer.analyze(args.focus)

    report_generator = ReportGenerator(analysis)

    if args.output == "stream":
        pprint.pprint(analysis)
    elif args.output == "json":
        if not args.outfile:
            print("Filename required for JSON output")
        else:
            report_generator.save_json(args.outfile)
    elif args.output == "txt":
        if not args.outfile:
            print("Filename required for TXT output")
        else:
            report_generator.save_txt(args.outfile)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
