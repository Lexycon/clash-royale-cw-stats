import urllib.request
import re
from Clanwars import Clanwars
from Player import Player

class StatsRoyaleParser:

    def __init__(self, clanId):
        self.clanId = clanId
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.106 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
    
    def callHTTPRequest(self, urlPath):
        request = urllib.request.Request('https://statsroyale.com/clan/' + self.clanId + urlPath, None, self.header)
        try:
            response = urllib.request.urlopen(request)
            return str(response.read(), 'utf-8')
        except e:
            raise MyException("There was an error: %r" % e)
        

    def refreshClan(self):
        urlPath = '/refresh'
        data = self.callHTTPRequest(urlPath)

    def getClanwars(self):
        urlPath = '/war/history'
        data = self.callHTTPRequest(urlPath)

        # Save local
        # with open('cr-cw-data.txt', 'w', encoding='utf-8') as the_file:
        #     the_file.write(data)
        # with open('cr-cw-data.txt', 'r', encoding='utf-8') as the_file:    
        #     data = the_file.read()


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

        clanwarIdCounter = 0
        clanwars = Clanwars()

        for match in regex.finditer(data):
            if (int(match.group(4)) == 1):
                clanwarIdCounter += 1

            player = clanwars.addPlayer(match.group(5), match.group(6))
            player.addClanwar(clanwarIdCounter, match.group(1), match.group(2), match.group(3))

        return clanwars



