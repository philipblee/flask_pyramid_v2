from Deck import *
from flask import Flask, render_template
from sort_cards import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/drag2')
def drag2():
    card_list = Deck.deal()[0]
    card_list = sorted(card_list, key=rank_sort, reverse=True)
    card_list = []
    card_path = []
    for card in card_list:
        card_path.append("static/Cards_gif/" + card[0:2] + ".gif")
    card_path = []
    return render_template("drag2.html", card_list=card_list, card_path=card_path)

@app.route('/deal25')
def deal25():
    card_list = Deck.deal()[0]
    card_list = sorted(card_list, key=rank_sort, reverse=True)
    print(card_list)
    card_path = []
    for card in card_list:
        card_path.append("static/Cards_gif/" + card[0:2] + ".gif")
    return render_template("drag2.html", card_list=card_list, card_path=card_path)


@app.route('/deal20')
def deal20():
    card_list = Deck.deal()[0][0:20]
    card_list = sorted(card_list, key=rank_sort, reverse=True)
    print(card_list)
    card_path = []
    for card in card_list:
        card_path.append("static/Cards_gif/" + card[0:2] + ".gif")
    return render_template("drag2.html", card_list=card_list, card_path=card_path)

@app.route('/deal')
def deal():
    card_list = Deck.deal()[0]
    card_list = sorted(card_list, key=rank_sort, reverse=True)
    print(card_list)
    card_path = []
    for card in card_list:
        card_path.append("static/Cards_gif/" + card[0:2] + ".gif")

    return render_template("deal.html", card_list=card_list, card_path=card_path)

if __name__ == '__main__':
    app.run(debug=True)