from Player import Player
from Clanwar import Clanwar
import csv

class Clanwars:
    
    def __init__(self):
        self.playerList = []
        self.warMode = ""

    def setWarMode(self, mode):
        self.warMode = mode

    def getWarMode(self):
        return self.warMode

    def addPlayer(self, id, name):
        player = self.getPlayerById(id)
        if player is None:
            player = Player(id, name)
            self.playerList.append(player)
        return player

    def getPlayerById(self, id):
        for player in self.playerList:
            if player.getId() == id:
                return player
        return None

    def getPlayerByName(self, name):
        for player in self.playerList:
            if player.getName().lower() == name.lower():
                return player
        return None

    def printPlayerById(self, id):
        print(self.getPlayerById(id))

    def printPlayerByName(self, name):
        print(self.getPlayerByName(name))

    def createCSVFile(self, file):
        with open(file, 'w', encoding='utf-8') as csvfile:
            # write csv header
            headers = ["ID", "Name", "Wins", "Battles", "Cards", "Live" + self.warMode, "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10"]
            dictWriter = csv.DictWriter(csvfile, headers, delimiter = ',')
            dictWriter.writeheader()

            # sort players alphabetically
            self.playerList.sort(key=lambda x: x.getName().lower())

            # write csv data
            writer = csv.writer(csvfile, delimiter='\n', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            writer.writerow(self.playerList)
