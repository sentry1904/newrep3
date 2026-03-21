import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Example data
    categories = ["Development", "Testing", "Documentation", "Deployment"]
    values = [40, 25, 20, 15]

    # Create pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=categories, autopct="%1.1f%%", startangle=90)
    plt.title("Project Work Distribution")
    plt.show()   # This opens a window with the chart if a GUI is available


