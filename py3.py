import matplotlib.pyplot as plt
import numpy as np

def ascii_line_chart(values, label="Data"):
    max_val = max(values)
    scale = 50  # max width in characters
    print(f"\nASCII Line Chart for {label}:\n")
    for i, v in enumerate(values):
        bar = "#" * int((v / max_val) * scale)
        print(f"{i:02d}: {bar} ({v})")

if __name__ == "__main__":
    # Generate some sample data (sine wave)
    x = np.linspace(0, 2 * np.pi, 20)
    y = np.sin(x) * 100  # scale for visibility

    # Print ASCII chart in Jenkins console
    ascii_line_chart([int(val) for val in y], label="Sine Wave")

    # Save a proper matplotlib graph as artifact
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, marker="o", color="blue", label="Sine Wave")
    plt.title("Sine Wave Example")
    plt.xlabel("X values")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.savefig("sine_wave.png")

    print("\nGraph saved as sine_wave.png (archive this in Jenkins to view).")

