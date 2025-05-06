from flask import Flask, render_template
import random as rnd

app = Flask(__name__)
rnd_num = rnd.randint(1, 100)

@app.route("/")
def home():
    #return f"<p>Hello, World!--{rnd_num}</p>"
    return render_template("index.html")

@app.route("/miguel")
def miguel():
    #return "Goodbye, World!"
    return render_template("cv/miguel.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True) 