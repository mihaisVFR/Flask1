from flask import Flask, json, request
from random import choice

app = Flask(__name__)
json.provider.DefaultJSONProvider.ensure_ascii = False


quotes = [
    {
        "id": 2,
        "author": "Rick Cook",
        "text": "Цитата для теста поиска по рейтингу.",
        "rating": 4
    },
    {
        "id": 3,
        "author": "Rick Cook",
        "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы "
                "с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов."
                " Пока вселенная побеждает.",
        "rating": 5
    },

    {
        "id": 5,
        "author": "Waldi Ravens",
        "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей "
                "с острыми бритвами в руках.",
        "rating": 3
    },
    {
        "id": 6,
        "author": "Mosher’s Law of Software Engineering",
        "text": "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили.",
        "rating": 4
    },
    {
        "id": 8,
        "author": "Yoggi Berra",
        "text": "В теории, теория и практика неразделимы. На практике это не так.",
        "rating": 5
    },

]


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


def new_id():
    return quotes[-1]["id"] + 1


@app.route("/quotes", methods=['POST'])
def create_quote():
    new_quote = request.json
    new_quote["id"] = new_id()
    if not new_quote.get("rating"):
        new_quote["rating"] = 1
    quotes.append(new_quote)
    return new_quote, 201


@app.route("/quotes/<int:quote_id>", methods=['PUT'])
def edit_quote(quote_id):
    new_data = request.json
    for quote in quotes:
        if quote["id"] == quote_id:

            if new_data.get("author"):
                quote["author"] = new_data["author"]

            if new_data.get("text"):
                quote["text"] = new_data["text"]

            if new_data.get("rating"):
                if new_data.get("rating") < 6 or new_data.get("rating") < 1:
                    quote["rating"] = new_data["rating"]
            return quote, 200
    return f"Quote with id={quote_id} not found", 404


@app.route("/quotes/<int:quote_id>", methods=['DELETE'])
def delete(quote_id):
    for quote in quotes:
        if quote["id"] == quote_id:
            quotes.remove(quote)
    return f"Quote with id {quote_id} is deleted.", 200


@app.route('/quotes/filter', methods=['GET'])
def quote_search():
    args = request.args
    author = args.get("author", type=str)
    rating = args.get("rating", type=int)
    rating_min = args.get("rating_min", type=int)
    rating_max = args.get("rating_max", type=int)
    if None not in (author, rating):
        result = [quote for quote in quotes if author == quote["author"] and rating == quote["rating"]]
        return result
    if None not in (rating_min, rating_max):
        result = [quote for quote in quotes if rating_min <= quote["rating"] <= rating_max]
        return result
    if author is not None:
        result = [quote for quote in quotes if author == quote["author"]]
        return result
    if rating is not None:
        result = [quote for quote in quotes if rating == quote["rating"]]
        return result
