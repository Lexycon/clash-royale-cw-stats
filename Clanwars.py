from Player import Player
from Clanwar import Clanwar
import csv

class Clanwars:
    
    def __init__(self):
        self.playerList = []

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
        with open(file, 'w') as csvfile:
            headers = ["ID", "Name", "Wins", "Battles", "Cards", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10"]
            dictWriter = csv.DictWriter(csvfile, headers, delimiter = ',')
            dictWriter.writeheader()

            writer = csv.writer(csvfile, delimiter='\n', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            writer.writerow(self.playerList)
