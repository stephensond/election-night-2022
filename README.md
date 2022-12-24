# Election night 2022

`election_night.py` is a quick script to translate the data from 538's 2022 election model into various csv files using `pandas`, to help me more easily follow the most competitve house, senate, and gubernatorial races on election night.

Input csv files, located in the `input` directory, are downloaded directly from 538. 

[https://projects.fivethirtyeight.com/2022-election-forecast/](https://projects.fivethirtyeight.com/2022-election-forecast/)

Output csv files are located in the `output` directory. Here is the data each output csv file contains:

- `gov_all.csv`: all gubernatoral elections, sorted by expected margin
- `gov_competitve.csv`: all gubernatorial elections expected to be within 10 points, sorted by expected margin
- `house_all.csv`: all house elections, sorted by expected margin
- `house_by_state_all.csv`: all house elections, sorted by state
- `house_by_state_competitive.csv`: all house elections expected to be within 10 points, sorted by state
- `house_competitve.csv`: all house elections expected to be within 10 points, sorted by expected margin
- `senate_all.csv`: all senate elections, sorted by expected margin
- `senate_competitve.csv`: all senate elections expected to be within 10 points, sorted by expected margin

Each output csv file only includes the most relevant information about each election:

- `district`: name of the contested seat
- `net`: the expected margin, where `-10` means an expected 10 point R win, and `10` means an expected 10 point D win
- `D`: name of the Democratic candidate
- `D vote`: expected vote share of the Democratic candidate
- `R`: name of the Republican candidate
- `R vote`: and expected vote share of the Republican candidate
