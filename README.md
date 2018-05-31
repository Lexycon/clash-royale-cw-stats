clash-royale-cw-stats
-------------

Simple python statsroyale parser for better clanwar evaluation. Data (last 10 wars) can be exported to a csv file and displayed by d3js.

statsroyale: [https://statsroyale.com](https://statsroyale.com)


## Usage

example clan (Brasil eSports): [https://statsroyale.com/de/clan/8RU0G892](https://statsroyale.com/de/clan/8RU0G892)

example player (Palitovsk): [https://statsroyale.com/de/profile/P0GVVY2G](https://statsroyale.com/de/profile/P0GVVY2G)


to generate csv list of clanwars:
```python
python main.py -r -c 8RU0G892 -o cr-cw-list.csv

# format csv file:

# ID,Name,(Sum)Wins,(Sum)Battles,(Sum)Cards,#1,#2,#3,#4,#5,#6,#7,#8,#9,#10
# [#1-#10] = Cards(collection day);Wins(war day);Battles(war day)
```


to print user clanwars by id or name:
```python
python main.py -r -c 8RU0G892 -u P0GVVY2G
# OR
python main.py -r -c 8RU0G892 -n Palitovsk

# print: P0GVVY2G,"Palitovsk",10,11,8436,1487;2;2,1020;1;1,1189;2;2,850;0;1,;;,850;1;1,640;1;1,960;1;1,640;1;1,800;1;1
```

Open index.html in Browser to display csv file.


## Todo

* more evaluation
* refactoring