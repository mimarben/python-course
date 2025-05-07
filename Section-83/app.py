from flask import Flask, render_template

app = Flask(__name__)

# Example data: add your own projects and skills!
projects = [
    {
        'name': 'Morse Code Converter',
        'description': 'A Python program that converts text to Morse code.',
        'link': 'https://github.com/yourusername/morse-code-converter'
    },
    {
        'name': 'Weather App',
        'description': 'A web app that shows weather info using an API.',
        'link': 'https://github.com/yourusername/weather-app'
    }
]

skills = ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript', 'APIs']

@app.route('/')
def home():
    return render_template('index.html', projects=projects, skills=skills)

if __name__ == '__main__':
    app.run(debug=True)
