import argparse
import analyze

def main():
    '''
    Main function that initializes the analyzer. 
    '''
    parser = argparse.ArgumentParser(description="Analyze a text file and generate reports in various formats.")
    parser.add_argument("input_file", help="Path to the input text file")
    parser.add_argument("--text", help="Output path for the text report")

    args = parser.parse_args()

    with open(args.input_file, 'r') as file:
        text = file.read()
        
    analysis = analyze.analyze_text(text)

    print(analysis)

if __name__ == "__main__":
    main()
