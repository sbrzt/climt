# main.py

import argparse
import pprint
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
    parser.add_argument(
        "--viz",
        choices=[
            "table",
            "plot",
            "image"
        ],
        help="Visualization type"
    )

    args = parser.parse_args()

    if args.files:
        texts = [load_files(f) for f in args.files]
        text = "\n\n".join(texts)
    elif args.input:
        text = args.input
    else:
        raise Exception("No input text or file provided.")
        
    analyzer = Analyzer(text)
    analyzer.plug_modules(args.analyze)
    analyzer.generate_analysis()
    analysis = analyzer.analysis

    if args.viz:
        for module in analyzer.modules:
            if module.name in args.analyze:
                if args.viz == "table" and hasattr(module, "print_table"):
                    module.print_table()
                elif args.viz == "plot" and hasattr(module, "print_plot"):
                    module.print_plot()
                elif args.viz == "image" and hasattr(module, "save_plot"):
                    module.save_plot()

    if args.output == "stream":
        pprint.pprint(analysis)
    else:
        if not args.outfile:
            print(f"Filename required for .{args.output} output")
        else:
            save_report(analysis, args.outfile, args.output)
    
if __name__ == "__main__":
    main()
