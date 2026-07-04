import json
from pathlib import Path

from flask import Flask, abort, render_template

app = Flask(__name__)

CARD_TEMPLATES = {
    "africa": "cards/africa.html",
    "america-do-norte": "cards/america-do-norte.html",
    "america-do-sul": "cards/america-do-sul.html",
    "antartida": "cards/antartida.html",
    "asia": "cards/asia.html",
    "europa": "cards/europa.html",
    "oceania": "cards/oceania.html",
}

SLUG_TO_CONTINENT = {
    "africa": "África",
    "america-do-norte": "América do Norte",
    "america-do-sul": "América do Sul",
    "antartida": "Antártida",
    "asia": "Ásia",
    "europa": "Europa",
    "oceania": "Oceania",
}

def load_authors():
    # Load info.json from the app/data directory
    json_path = Path(app.root_path) / "data" / "info.json"
    if json_path.exists():
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            app.logger.error(f"Error loading info.json: {e}")
    return []

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cards/<slug>")
def card(slug: str):
    template_path = CARD_TEMPLATES.get(slug)
    if not template_path:
        abort(404)

    file_exists = (Path(app.root_path) / (app.template_folder or "templates") / template_path).exists()
    if not file_exists:
        abort(404)

    continent_name = SLUG_TO_CONTINENT.get(slug)
    all_authors = load_authors()
    
    # Filter authors belonging to this continent
    authors = [a for a in all_authors if a.get("continent") == continent_name]

    return render_template(template_path, authors=authors, title=continent_name)


if __name__ == "__main__":
    app.run(debug=True, port=5008)

