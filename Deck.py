from random import shuffle

suit = 'SHDC'
rank = 'AKQJT98765432'
deck_number = '+-*'
deck = [s + r + d for s in suit for r in rank for d in deck_number] # deck is list of cards
deck.extend(["WW+", "WW-", "WW*"]) # appends 3 wild cards to deck

class Deck:
    def __init__(self):
        pass

    @staticmethod
    def deal(n=6):
        for i in range(1):
            shuffle(deck)
        pyramid_poker_list = [HandDeck(deck[i::n]) for i in range(n)]
        return [pyramid_poker_list[0][0:25]]

    # @staticmethod
    # def deal_6hands(n=6):
    #     for i in range(2):
    #         shuffle(deck)
    #     pyramid_poker_list = [HandDeck(deck[i:150:n]) for i in range(n)]
    #     return [pyramid_poker_list]
    #
    # def deal_3deck(self, n=1):
    #     return [list(deck[i::n]) for i in range(n)]

class HandDeck(list):
    pass
