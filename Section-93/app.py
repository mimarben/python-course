from flask import Flask, render_template
from scraper import scrape_nba_player_stats

app = Flask(__name__)

@app.route("/")
def index():
    stats = scrape_nba_player_stats()
    return render_template("index.html", stats=stats)

if __name__ == "__main__":
    app.run(debug=True)
