clash-royale-cw-stats
-------------

Simple Python statsroyale.com parser for better clanwar evaluation. Data (Collection/War Day + last 10 wars) can be exported to a CSV file and displayed by d3js.

statsroyale: [https://statsroyale.com](https://statsroyale.com)

## Usage

Example:

Clan (Brasil eSports) ID: [8RU0G892](https://statsroyale.com/de/clan/8RU0G892)

Player (Andrelds) ID: [2PJC0R2VG](https://statsroyale.com/de/profile/2PJC0R2VG)


To generate CSV file (check output csv example: [CSV file](https://github.com/Lexycon/clash-royale-cw-stats/blob/master/web/cr-cw-list.csv)):
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
The 'Live' column can be Collection Day or War day. The Collection Day Wins/Battles won't count to the global user stats.

### Colors

- <span style="color:#eea6ee">purple</span>: Collection Day
- <span style="color:#b2eea6">green</span>: All matches won (War Day)
- <span style="color:#eed5a6">orange</span>: At least 1 but not all matches won (War Day)
- <span style="color:#eea6a6">red</span>: No match won (War Day)
- <span style="color:#a6cfee">blue</span>: Not played (War Day) but collected (Collection Day)
- <span style="color:#dedede">grey</span>: Not participated

## Screenshot

![preview.png](https://github.com/Lexycon/clash-royale-cw-stats/blob/master/preview.png)


## Todo

* more evaluation
* refactoring
* better design :)