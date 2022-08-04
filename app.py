from Deck import *
from flask import Flask, render_template
from sort_cards import *


app = Flask(__name__)

def show_next_hand(*args):
    """ Create the card list use Deck().deal and display_cardlist them"""
    global twentyfive_cards
    twentyfive_cards = Deck.deal()

@app.route('/')
def index():
    show_next_hand()
    global twentyfive_cards
    twenty_cards = (sorted(twentyfive_cards[0][0:20], key=rank_sort, reverse=True))
    kitty_cards = (sorted(twentyfive_cards[0][20:25], key=rank_sort, reverse=True))
    twentyfive_cards = twenty_cards + kitty_cards
    print (twentyfive_cards)
    card_path = []
    for card in twentyfive_cards:
        card_path.append("static/Cards_gif/" + card[0:2] + ".gif")
    return render_template("new_hand.html", card_list=twentyfive_cards, card_path=card_path)

@app.route('/show_kitty')
def show_kitty():
    global twentyfive_cards
    card_path = []
    for card in twentyfive_cards:
        card_path.append("static/Cards_gif/" + card[0:2] + ".gif")
    return render_template("show_kitty.html", card_list=twentyfive_cards, card_path=card_path)

if __name__ == '__main__':
    app.run(debug=True)