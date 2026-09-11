from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "title": "Project One",
        "description": "Desc",
        "link": "link",
        "image": "link",
    },
    {
        "title": "Project two",
        "description": "Desc",
        "link": "link",
        "image": "link",
    },
]

@app.route("/")
def home():
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


