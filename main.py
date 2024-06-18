import argparse
import analyze, produce

def main():
    '''
    Main function that initializes the analyzer. 
    '''
    parser = argparse.ArgumentParser(description="Analyze a text file and generate reports in various formats.")
    parser.add_argument("input", nargs='?', help="Path to the input text file")
    parser.add_argument("--file", help="Path to the input text file")
    parser.add_argument("--output", choices=["stream", "csv"], default="stream", help="Output format")
    parser.add_argument("--outfile", help="Output file name")

    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as f:
            text = f.read()
    elif args.input:
        text = args.input
    else:
        print("No input text or file provided.")
        return
        
    analysis = analyze.analyze_text(text)

    if args.output == "stream":
        produce.print_table(analysis)
    elif args.output == "csv":
        if not args.outfile:
            print("Filename required for csv output")
        else:
            produce.save_csv(analysis, args.outfile)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
