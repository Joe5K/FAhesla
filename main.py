from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

PASSWORD = {
    0: "5612",
    1: "32276",
    2: "BZCD",
    3: "M4B2",
    4: "Z+1C",
}

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        if request.form["password"] == PASSWORD.get(int(request.form["level"])):
            return "OK"
        else:
            return "KO"
    return render_template("template.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, threaded=True)
