from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import random
import os
import signal

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = None

    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            try:
                val = int(user_input)
                if val == 100:
                    message = "Received 100 — stopping Flask..."
                    os.kill(os.getpid(), signal.SIGTERM)
                else:
                    message = f"Received input: {val}"
            except ValueError:
                message = "Please enter a valid integer."

        # Generate random chart
        values = [random.randint(1, 50) for _ in range(10)]
        plt.figure(figsize=(6, 4))
        plt.plot(values, marker="o", linestyle="-", color="blue")
        plt.title("Random Values Chart")
        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.grid(True)

        # Ensure static directory exists
        chart_dir = os.path.join(app.root_path, "static")
        os.makedirs(chart_dir, exist_ok=True)

        chart_path = os.path.join(chart_dir, "chart.png")
        plt.savefig(chart_path)
        plt.close()

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

