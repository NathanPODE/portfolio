from flask import Flask, render_template

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
    app.run(debug=True, host="0.0.0.0", port=5000)


