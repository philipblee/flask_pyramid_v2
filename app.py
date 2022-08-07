from Deck import *
from flask import Flask, render_template
from sort_cards import *

# submit button
# login
# sort by suit and rank

app = Flask(__name__)

def show_next_hand(*args):
    """ Create the card list use Deck().deal and display_cardlist them"""
    global twentyfive_cards
    twentyfive_cards = Deck.deal()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/new_hand')
def new_hand():
    show_next_hand()
    global twentyfive_cards, rank_sorted_cards, suit_sorted_cards
    twenty_cards = (sorted(twentyfive_cards[0][0:20], key=rank_sort, reverse=True))
    kitty_cards = (sorted(twentyfive_cards[0][20:25], key=rank_sort, reverse=True))
    rank_sorted_cards = (sorted(twentyfive_cards[0][0:25], key=rank_sort, reverse=True))
    suit_sorted_cards = (sorted(twentyfive_cards[0][0:25], key=suit_rank_sort, reverse=True))
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
    return render_template("sorted.html", card_list=twentyfive_cards, card_path=card_path)

@app.route('/sort_by_rank')
def sort_by_rank():
    global twentyfive_cards, rank_sorted_cards, suit_sorted_cards
    print ("sort by rank")
    card_path = []
    print (rank_sorted_cards)
    for card in rank_sorted_cards:
        card_path.append("static/Cards_gif/" + card[0:2] + ".gif")
    return render_template("sorted.html", card_list=rank_sorted_cards, card_path=card_path)

@app.route('/sort_by_suit')
def sort_by_suit():
    global twentyfive_cards, rank_sorted_cards, suit_sorted_cards
    print ("sort by suit")
    print (suit_sorted_cards)
    card_path = []
    for card in suit_sorted_cards:
        card_path.append("static/Cards_gif/" + card[0:2] + ".gif")
    return render_template("sorted.html", card_list=suit_sorted_cards, card_path=card_path)

if __name__ == '__main__':
    app.run(debug=True)