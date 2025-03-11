from flask import Flask
import random as rnd
app = Flask(__name__)
rnd_num = rnd.randint(1, 100)

@app.route("/")
def hello_world():
    return f"<p>Hello, World!--{rnd_num}</p>"

if __name__ == "__main__":
    app.run(debug=True) 