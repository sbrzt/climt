from tabulate import tabulate

def print_table(analysis):
    headers = ["Word", "Occurrences", "Frequency (%)", "POS Tag", "Lemma", "Senses"]
    table = [[
        detail['word'],
        detail['occurrences'],
        f"{detail['frequency_percent']:.2f}",
        detail['pos_tag'],
        detail['lemma'],
        ", ".join(detail['senses'])
    ] for detail in analysis['word_details']]
    
    return tabulate(table, headers=headers)