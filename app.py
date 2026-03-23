from flask import Flask, render_template, request
import os
import signal

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def dashboard():
    message = None
    if request.method == "POST":
        user_input = request.form.get("user_input")

        if user_input == "100":
            message = "Pipeline cleanup triggered!"
            # Exit Flask immediately so Jenkins knows to stop
            os.kill(os.getpid(), signal.SIGTERM)
        else:
            message = f"You entered: {user_input}"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

