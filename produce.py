from tabulate import tabulate
import csv

headers = [
    "Word", 
    "Occurrences", 
    "Frequency (%)", 
    "POS Tag", 
    "Lemma", 
    "Senses"]

def generate_rows(analysis):
    rows = [[
        detail['word'],
        detail['occurrences'],
        f"{detail['frequency_percent']:.2f}",
        detail['pos_tag'],
        detail['lemma'],
        ", ".join(detail['senses'])
    ] for detail in analysis['word_details']]
    return rows


def print_table(analysis):
    return tabulate(generate_rows(analysis), headers=headers)

def save_csv(analysis, filename):
    with open(filename, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)
        csvwriter.writerows(generate_rows(analysis))