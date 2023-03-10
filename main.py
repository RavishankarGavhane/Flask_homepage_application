from flask import Flask, render_template, abort, jsonify
from models.dal import db


app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html", cards=db)

@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template(
            "card.html",
            card=card,
            index=index,
            max_card=len(db) - 1
        )
    except IndexError:
        abort(404)

@app.route("/api/cards")
def api_card_list():
    return jsonify(db)




