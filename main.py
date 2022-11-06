from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
app.debug = True

PASSWORD = {
    0: "5612",
    1: "32276",
    2: "BZCD",
    3: "M4B2",
    4: "Z+1C",
}

BRUTEFORCE_SECURED = False
last_wrong = datetime.fromtimestamp(0)

@app.route('/', methods=["GET", "POST"])
def hello_world():
    global last_wrong
    if request.method == "POST" and (input_password := request.form.get("password")):
        while BRUTEFORCE_SECURED and (datetime.now() - last_wrong).total_seconds() < 5:
            pass  # programmer lvl 200

        if input_password == PASSWORD.get(int(request.form["level"])):
            return "OK"
        else:
            last_wrong = datetime.now()
            return "KO"
    return render_template("template.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, threaded=True)
