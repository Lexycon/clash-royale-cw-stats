import urllib.request
import re
from Clanwars import Clanwars
from Player import Player

class StatsRoyaleParser:

    def __init__(self, clanId):
        self.clanwarIdCounter = -1
        self.clanwars = Clanwars()
        self.clanId = clanId
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.106 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Language': 'en-US,en;q=0.8'}
    
    def callHTTPRequest(self, urlPath):
        url = 'https://statsroyale.com/clan/' + self.clanId + urlPath
        print("Requesting: " + url)

        request = urllib.request.Request(url, None, self.header)
        try:
            response = urllib.request.urlopen(request, timeout=10)
            return str(response.read(), 'utf-8')
        except e:
            raise MyException("There was an error: %r" % e)
        

    def refreshClan(self):
        urlPath = '/refresh'
        data = self.callHTTPRequest(urlPath)

    def parseClanwar(self):
        urlPath = '/war'
        data = self.callHTTPRequest(urlPath)

        # get warMode
        if ("Collection Day" in data): self.clanwars.setWarMode("Col")
        elif ("War Day" in data): self.clanwars.setWarMode("War")

        self.parse(data)
        # if no collection/war day detected -> 
        # iterate clanwarId anyways to get empty live column
        if (self.clanwarIdCounter == -1): self.clanwarIdCounter += 1

    def parseClanwarsHistory(self):
        urlPath = '/war/history'
        data = self.callHTTPRequest(urlPath)
        self.parse(data)

    def parse(self, data):
        pattern = ('data-cards="(\d+)" data-wins="(\d+)" data-battles="(\d+)">\n' +
            '.*?>#(\d+)</div>\n.*?\n' +
            '.*/profile/(.+?)".*>(.+?)</a>')
            # (1) cards collected
            # (2) clanwar wins 
            # (3) clanwar battles
            # (4) rank
            # (5) playerid
            # (6) name
        regex = re.compile(pattern)

        for match in regex.finditer(data):
            # rank of player in clanwar is used to detect which clanwar is parsed
            # if #1 of player appears -> new/other clanwar data
            if (int(match.group(4)) == 1):
                self.clanwarIdCounter += 1
            
            # add player if not exists, else return existing player object
            player = self.clanwars.addPlayer(match.group(5), match.group(6))
        
            # add clanwar to player
            player.addClanwar(self.clanwarIdCounter, match.group(1), match.group(2), match.group(3), self.clanwars.getWarMode())

        

    def getClanwars(self):
        return self.clanwars


