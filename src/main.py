# main.py

import argparse
import pprint
from pathlib import Path
from analyzer import Analyzer
from utils.report import save_report
from utils.load import load_files


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
        "--files",
        nargs="+",
        help="Path(s) to one or more input documents"
    )
    parser.add_argument(
        "--multi-mode",
        choices=["merge", "separate"],
        default="merge",
        help="How to handle multiple input files: 'merge' into one analysis or 'separate' analyses."
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
        "--analyze", 
        nargs='*', 
        choices=[
            "text",
            "words",
            "pos",
            "read",
            "sent"
        ], 
        default=["text"], 
        help="Focus of the analysis"
    )


    args = parser.parse_args()

    if args.files:
        texts = load_files(args.files)
        if args.multi_mode == "merge":
            text = "\n\n".join(texts)
            analyzer = Analyzer(text)
            analyzer.plug_modules(args.analyze)
            analyzer.generate_analysis()
            analysis = analyzer.analysis
            save_report(analysis, args.outfile, args.output)
        else:
            for filepath, text in zip(args.files, texts):
                analyzer = Analyzer(text)
                analyzer.plug_modules(args.analyze)
                analyzer.generate_analysis()
                analysis = analyzer.analysis
                base = Path(filepath).stem
                save_report(analysis, f"{base}_{args.outfile}", args.output)
    elif args.input:
        text = args.input
        analyzer = Analyzer(text)
        analyzer.plug_modules(args.analyze)
        analyzer.generate_analysis()
        analysis = analyzer.analysis
        save_report(analysis, args.outfile, args.output)
    else:
        raise Exception("No input text or file provided.")

    if args.output == "stream":
        pprint.pprint(analysis)
    else:
        if not args.outfile:
            print(f"Filename required for .{args.output} output")
        else:
            save_report(analysis, args.outfile, args.output)
    
if __name__ == "__main__":
    main()
