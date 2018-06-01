import sys
from argparse import ArgumentParser
from Clanwars import Clanwars
from StatsRoyaleParser import StatsRoyaleParser

parser = ArgumentParser()
parser.add_argument("-r", "--refresh", dest="refresh", default=False, action="store_true", help="call refresh clan at statsroyale first")
parser.add_argument("-c", "--clanid", dest="clanid", type=str, required=True)

group = parser.add_mutually_exclusive_group()
group.add_argument("-o", "--output", dest="outfile", type=str, help="csv output file")
group.add_argument("-u", "--userid", dest="userid", type=str, help="get user clanwar data by id")
group.add_argument("-n", "--username", dest="username", type=str, help="get user clanwar data by name")
args = parser.parse_args()


statsRoyaleParser = StatsRoyaleParser(args.clanid)

if args.refresh:
    statsRoyaleParser.refreshClan()

# parse live (collection day or war day) clanwar 
statsRoyaleParser.parseClanwar()
# parse history clanwars (max. last 10) 
statsRoyaleParser.parseClanwarsHistory()
# get clanwars object
clanwars = statsRoyaleParser.getClanwars()

if args.outfile:
    clanwars.createCSVFile(args.outfile)

elif args.userid:
   clanwars.printPlayerById(args.userid)

elif args.username:
    clanwars.printPlayerByName(args.username)
