clash-royale-cw-stats
-------------

Simple Python statsroyale.com parser for better clanwar evaluation. Data (Collection/War Day + last 10 wars) can be exported to a CSV file and displayed by d3js.

statsroyale: [https://statsroyale.com](https://statsroyale.com)

## Usage

Example:

Clan (Brasil eSports) ID: [8RU0G892](https://statsroyale.com/de/clan/8RU0G892)

Player (Andrelds) ID: [2PJC0R2VG](https://statsroyale.com/de/profile/2PJC0R2VG)


To generate CSV file (check output CSV example: [CSV file](https://github.com/Lexycon/clash-royale-cw-stats/blob/master/web/cr-cw-list.csv)):
```bash
python main.py -r -c 8RU0G892 -o web/cr-cw-list.csv
```


To print CSV line of clanwars by userid or username:
```bash
python main.py -r -c 8RU0G892 -u 2PJC0R2VG
# OR
python main.py -r -c 8RU0G892 -n Andrelds

# print: 2PJC0R2VG,"Andrelds",3,6,7029,680;2;2,1189;0;1,1400;0;1,960;1;1,1680;0;1,640;1;1,480;1;1,;;,;;,;;,;;
```
The parameter -r (refresh) will trigger the statsroyale.com refresh first, so the clan information will be up to date before parsing.

## View

With the web/index.html you can display the CSV in your browser using the d3js.csv function.
The 'Live' column can be Collection Day or War Day. The Collection Day Wins/Battles won't count to the global user stats.

### Colors
- ![#eea6ee](https://placehold.it/15/eea6ee/000000?text=+) `purple: Collection Day`
- ![#b2eea6](https://placehold.it/15/b2eea6/000000?text=+) `green: All matches won (War Day)`
- ![#eed5a6](https://placehold.it/15/eed5a6/000000?text=+) `orange: At least 1 but not all matches won (War Day)`
- ![#eea6a6](https://placehold.it/15/eea6a6/000000?text=+) `red: No match won (War Day)`
- ![#a6cfee](https://placehold.it/15/a6cfee/000000?text=+) `blue: Not played (War Day) but collected (Collection Day)`
- ![#dedede](https://placehold.it/15/dedede/000000?text=+) `grey: Not participated`

## Screenshot

![preview.png](https://github.com/Lexycon/clash-royale-cw-stats/blob/master/preview.png)


## Todo

* more evaluation
* refactoring
* better design :)