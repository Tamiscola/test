import random

class Deck:
    suits = ['H', 'D', 'C', 'S']
    values = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']

    def __init__(self):
        self._cards = []

        for value in Deck.values:
            for suit in Deck.suits:
                card = value + suit
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self, n):
        dealt_cards = []
        for _ in range(n):
            card = self._cards.pop()
            dealt_cards.append(card)
        return dealt_cards

    def sort_by_suit(self):
        sorted_suits = {'H': [], 'D': [], 'C': [], 'S': []}

        for card in self._cards:
            suit = card[:-1]
            sorted_suits[suit].append(card)

        self._cards = (
            sorted_suits['H'] +
            sorted_suits['D'] +
            sorted_suits['C'] +
            sorted_suits['S']
        )

    def contains(self, card):
        if card not in self._cards:
            return False
        return card

    def copy(self):
        new_deck = Deck()
        new_deck._cards = self._cards[:]
        return new_deck

    def get_cards(self):
        return self._cards[:]

    def __len__(self):
        return len(self._cards)


deck1 = Deck()
deck1.shuffle()
print(deck1.sort_by_suit())