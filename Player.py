from Clanwar import Clanwar

class Player:

    def __init__(self, id, name) :
        self.id = id
        self.name = name
        self.sumWins = 0
        self.sumBattles = 0
        self.sumCards = 0
        self.clanwarList = []

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def addClanwar(self, id, cards, wins, battles):
        self.clanwarList.append(Clanwar(id, cards, wins, battles))
        self.sumWins += int(wins)
        self.sumBattles += int(battles)
        self.sumCards += int(cards)

    def getClanwarsCSV(self):
        clanwarListCSV = []
        for x in range(0, 10):
            clanwarListCSV.append(';;')
        for clanwar in self.clanwarList:
            clanwarListCSV[clanwar.getId()-1] = str(clanwar)

        return ','.join(clanwarListCSV)


    def __repr__(self):
        return (str(self.id) + ',"' + str(self.name) + '",' + 
        str(self.sumWins) + ',' + str(self.sumBattles) + ',' + 
        str(self.sumCards) + ',' + self.getClanwarsCSV())