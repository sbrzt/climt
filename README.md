# CLIMT

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14994045.svg)](https://doi.org/10.5281/zenodo.14994045)


## Description

**CLIMT** (_**CLI** for **M**odular **T**ext data mining_) is a modular data engineering CLI tool for easily producing text mining reports in portable formats.

## Installation

First, create a virtual environment to manage the project's dependencies. 

Using `uv`:

```bash
uv init         # Initialize the project with uv
uv run          # The first run generates the .venv directory
```

Second, activate the virtual environment:

* On Windows:  
```bash
.\.venv\Scripts\activate
```

* On macOS and Linux:  
```bash
source .venv/bin/activate
```

Third, install the required dependencies:

```bash
uv add -r requirements.txt
```

Finally, install this project in editable mode so that the `climt` command is available:

```bash
uv pip install -e .
```

Now you can run the tool from the command line:
```bash
climt "This is a sample text." --analyze text words
```

## Usage

The software is designed to analyze a text or a text file and generate reports in various formats. The user can interact with the software via the command line using several options for customization.

### Basic command structure

```bash
climt [input] [options]
```

It is possible to type the command directly in the command line, or type it in the `run.sh` file and then run it via

```bash
./run.sh
```

### Arguments and options

* `input` (Optional): A string representing the raw text to analyze. If not provided, you must specify a file using the `--file` option.
* `--file` (Optional): This specifies the path to a text file containing the content to analyze. It is an alternative to providing raw text directly.
* `--output` (Optional): This option allows you to specify the format of the output report. You can choose from the following:
    * `stream` (default): The output is printed directly to the command line.
    * `txt` or `md`: The output is saved as a plain text file or in a Markdown file.
* `--outfile `(Optional): If you select any option other than `stream` as the output format, you can provide a file name for the output file. If not specified, the file will be named according to the format (e.g., `output.txt` or `output.md`).
* `--analyze` (Optional): This option allows you to specify the focus of the analysis. The available choices are:
    * `text` (default): Performs a general statistical analysis on the text.
    * `words`: Performs a statistical analysis on each word in the text. Also allows generating visualizations for word frequencies.
    * `pos`: Performs a statistical Part-of-Speech (PoS) analysis on the text. Also allows generating visualizations for PoS frequencies.
    * `read`: Performs a readability analysis on the text.
    * `sent`: Performs a sentiment analysis on the text.

You can provide multiple analysis focuses by separating them with space (e.g. `--analyze text words read`).

### Examples

#### Analyze raw text and print the report in the terminal

```bash
climt "This is a sample text."
```

#### Analyze raw text and save the report in a .txt file

```bash
climt "This is a sample text." --output txt --outfile report.txt
```

#### Analyze a text file and save the report in a .md file

```bash
climt --files "input.txt" "other.txt" --output md --outfile report.md
```

## Testing

Run the following command in the terminal:

```bash
chmod +x test.sh

./test.sh
```

## Roadmap

- [x] Add more analysis modules;
- [ ] Implement better CLI UX design;
- [ ] Add other formats for report generation (JSON, XML, HTML);
- [ ] Add RDF conversion;
- [ ] Add visual graphs generation;
- [ ] Add research bundle generation.

## Author

Barzaghi, Sebastian (https://orcid.org/0000-0002-0799-1527).

## Citation

```
@software{barzaghi_2025_14994045,
  author       = {Barzaghi, Sebastian},
  title        = {CLIMT},
  month        = mar,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {v1.0.0},
  doi          = {10.5281/zenodo.14994045},
  url          = {https://doi.org/10.5281/zenodo.14994045},
  swhid        = {swh:1:dir:3ed76b26799f6c467462694f3fb559a7d6157fb4
                   ;origin=https://doi.org/10.5281/zenodo.14994044;vi
                   sit=swh:1:snp:6f73683da2edea4d58c9d324592251ddf66b
                   5a96;anchor=swh:1:rel:924dee9e6fa7d3674e5417ac593d
                   e2a32ac9701b;path=sbrzt-lodot-8ea7eb0
                  },
}
```
