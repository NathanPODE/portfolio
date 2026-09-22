from flask import Flask, render_template
import os

app = Flask(__name__)

projects = [
    {
        "title": "Task Attacker",
        "link": "https://github.com/uhhitsnathan/comp380-group-project",
        "image": "images/task-attacker.png",
    },
    {
        "title": "This Website",
        "link": "https://github.com/NathanPODE/portfolio",
        "image": "images/portfolio.png",
    },
]

@app.route("/")
def home():
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    debug_mode = os.environ.get("FLASK_DEBUG", "true").lower() == "true"
    app.run(debug=debug_mode, host="0.0.0.0", port=port)


