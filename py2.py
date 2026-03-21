import matplotlib.pyplot as plt
import numpy as np

def ascii_bar_chart(data, labels):
    max_val = max(data)
    scale = 50  # max width of bar in characters
    for label, value in zip(labels, data):
        bar = "#" * int((value / max_val) * scale)
        print(f"{label:10} | {bar} ({value})")

if __name__ == "__main__":
    # Example data
    labels = ["Task A", "Task B", "Task C", "Task D"]
    values = np.random.randint(5, 100, size=len(labels))

    print("ASCII Bar Chart of Random Values:\n")
    ascii_bar_chart(values, labels)

    # Also show a summary with matplotlib (saved as text backend)
    plt.switch_backend("Agg")  # ensures no GUI
    plt.bar(labels, values)
    plt.title("Random Values per Task")
    plt.xlabel("Tasks")
    plt.ylabel("Value")
    plt.savefig("chart.png")  # saved as artifact if Jenkins archives it
    print("\nGraph also saved as chart.png for artifacts.")

