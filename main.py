import argparse
import analyze

def main():
    '''
    Main function that initializes the analyzer. 
    '''
    parser = argparse.ArgumentParser(description="Analyze a text file and generate reports in various formats.")
    parser.add_argument("input", help="Path to the input text file")
    parser.add_argument("--output", help="Output path for the text report")
    #parser.add_argument(
    # '--output_format', 
    # type=str, 
    # choices=['txt', 'csv', 'rdf'], 
    # default='txt', 
    # help="Output report format"
    # )

    args = parser.parse_args()

    with open(args.input, 'r') as file:
        text = file.read()
        
    analysis = analyze.analyze_text(text)

    print(analysis)

if __name__ == "__main__":
    main()
