class Clanwar: 

    def __init__(self, id, cards, wins, battles):
        self.id = id
        self.cards = cards
        self.wins = wins
        self.battles = battles

    def getId(self):
        return self.id

    def getCards(self):
        return self.cards

    def getWins(self):
        return self.wins

    def getBattles(self):
        return self.battles

    def __repr__(self):
        return (str(self.cards) + ';' + str(self.wins) + ';' + str(self.battles))