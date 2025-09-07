# src/utils/visualization.py

import matplotlib.pyplot as plt


def print_table(
    data,
    headers=("Item", "Count", "Freq")
    ):
    h1, h2, h3 = headers
    print(f"{h1:<15}{h2:<10}{h3:<10}")
    for item, count, freq in data:
        print(f"{item:<10}{count:<10}{freq:<10.4f}")
    
def print_plot(
    data, 
    max_width=60, 
    symbol="#"
    ):
    max_count = max(count for _, count, _ in data)
    for item, count, freq in data:
        bar = symbol * int(count / max_count * max_width)
        print(f"{item:<10}{count:<5}{bar}")

def save_plot(
    data, 
    filename="plot.png",
    title="freqs",
    color="skyblue"
    ):
    items = [item for item, _, _ in data]
    counts = [count for _, count, _ in data]
    plt.figure(figsize=(10,6))
    plt.bar(items, counts, color=color)
    plt.xticks(rotation=45)
    plt.ylabel("Count")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()