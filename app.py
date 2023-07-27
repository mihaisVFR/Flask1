from flask import Flask, json
from random import choice

app = Flask(__name__)
json.provider.DefaultJSONProvider.ensure_ascii = False

about_me = {
    "name": "Плужников",
    "surname": "Михаил",
    "email": "someadres@somepost.ru"
}

quotes = [
    {
        "id": 3,
        "author": "Rick Cook",
        "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает."
    },
    {
        "id": 5,
        "author": "Waldi Ravens",
        "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей с острыми бритвами в руках."
    },
    {
        "id": 6,
        "author": "Mosher’s Law of Software Engineering",
        "text": "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили."
    },
    {
        "id": 8,
        "author": "Yoggi Berra",
        "text": "В теории, теория и практика неразделимы. На практике это не так."
    },

]


@app.route("/")
def hello_world():
    return "<p>Hello, World!!!</p>"


@app.route("/about")
def about_author():
    return about_me


@app.route("/quotes")
def get_quotes():
    return quotes


@app.route("/quotes/<int:quote_id>")
def get_quote_by_id(quote_id):
    for quote in quotes:
        if quote["id"] == quote_id:
            return quote

    return f"Quote with id={quote_id} not found", 404


@app.route("/quotes/count")
def quotes_count():
    return {
        "count": len(quotes)
    }


@app.route("/quotes/random")
def random_quote():
    return choice(quotes)
