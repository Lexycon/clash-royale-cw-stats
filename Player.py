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

    def addClanwar(self, id, cards, wins, battles, warMode):
        self.clanwarList.append(Clanwar(id, cards, wins, battles))
        self.sumCards += int(cards)
        # don't count collection day war wins/battles
        if (not (warMode == "Col" and id == 0)):
            self.sumWins += int(wins)
            self.sumBattles += int(battles)
        

    def getClanwarsCSV(self):
        # create empty csv row with 11 columns
        clanwarListCSV = []
        for x in range(0, 11):
            clanwarListCSV.append(';;')
        
        # replace empty columns where clanwar is available
        for clanwar in self.clanwarList:
            clanwarListCSV[clanwar.getId()] = str(clanwar)

        return ','.join(clanwarListCSV)


    def __repr__(self):
        return (str(self.id) + ',"' + str(self.name) + '",' + 
        str(self.sumWins) + ',' + str(self.sumBattles) + ',' + 
        str(self.sumCards) + ',' + self.getClanwarsCSV())