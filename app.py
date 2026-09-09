from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True, port=5000)


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