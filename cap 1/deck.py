import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')
print 'carta beer'
print beer_card

deck = FrenchDeck()
print 'tamanho do deck'
print len(deck)

print 'primeira carta do deck'
print deck[0]
print 'ultima carta do deck'
print deck[-1]


from random import choice
print 'carta aleatoria'
print choice(deck)
print 'carta aleatoria'
print choice(deck)
print 'carta aleatoria'
print choice(deck)

print 'cortando o baralho'
print deck[:3]
print 'cortando o baralho'
print deck[12::13]

print 'imprimir baralho'
for card in deck:
    print(card)

print 'imprimir baralho reverso'
for card in reversed(deck):
    print(card)
