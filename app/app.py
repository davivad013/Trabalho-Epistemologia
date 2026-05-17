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


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cards/<slug>")
def card(slug: str):
    template_path = CARD_TEMPLATES.get(slug)
    if not template_path:
        abort(404)

    file_exists = Path(app.template_folder or "templates", template_path).exists()
    if not file_exists:
        abort(404)

    return render_template(template_path)


if __name__ == "__main__":
    app.run(debug=True, port=5008)
