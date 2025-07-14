from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def insecure_warning():
    return render_template("force_https.html"), 403


if __name__ == "__main__":
    app.run(port=5000, debug=True)
