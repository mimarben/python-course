from flask import Flask, render_template
import datetime
import random
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = 100 * (1 + (random.random() * 0.2))  # generate a random number between 100 and 120
    current_year = datetime.datetime.now().year
    return render_template('index.html', num= random_number, year = current_year)
@app.route('/guest/<string:name>')
def guess(name):
    response_gender = requests.get(f"https://api.genderize.io/?name={name}")
    response_age = requests.get(f"https://api.agify.io/?name={name}")
    response_gender.raise_for_status()
    data_gender = response_gender.json()
    data_age = response_age.json()
    gender = (data_gender["gender"]);
    age = data_age["age"];
    gender = random.choice(['male', 'female'])
    age = random.randint(18, 99)  # generate a random age between 18 and 99
    return render_template('guess.html', name=name, gender = gender, age = age)

@app.route('/blog/')
def blog():
    response_articles = requests.get("https://api.npoint.io/8a5c08924b2368d67daa")
    blog_posts = response_articles.json()
    print(blog_posts)
    return render_template('blogs.html', blog_posts=blog_posts)

if __name__ == "__main__":
    app.run(debug=True)


