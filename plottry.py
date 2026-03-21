import plotext as plt

if __name__ == "__main__":
    # Example data
    categories = ["Development", "Testing", "Documentation", "Deployment"]
    values = [40, 25, 20, 15]

    print("\nPie Chart (Console Output):\n")

    # Plot pie chart directly in terminal
    plt.pie(values, labels = categories)
    plt.title("Project Work Distribution")
    plt.show()

