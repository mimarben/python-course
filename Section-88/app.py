from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    map_url = db.Column(db.String(300))
    wifi_strength = db.Column(db.String(100))
    has_power = db.Column(db.Boolean, default=False)
    coffee_rating = db.Column(db.String(100))

# Routes
@app.route("/")
def home():
    cafes = Cafe.query.all()
    return render_template("index.html", cafes=cafes)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_cafe = Cafe(
            name=request.form["name"],
            location=request.form["location"],
            map_url=request.form["map_url"],
            wifi_strength=request.form["wifi_strength"],
            has_power=bool(request.form.get("has_power")),
            coffee_rating=request.form["coffee_rating"]
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/delete/<int:cafe_id>")
def delete(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
