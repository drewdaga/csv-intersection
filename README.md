# csv-intersection
Print the intersection of two CSV files

A very naive python script that compares every cell of one csv to every cell of another and returns the list of similar cells. More than sufficient for now and don’t need to worry about them changing the order of columns or anything.

Usage: 
```
drew@WINDOWS10:~/csv-intersection$ python3 main.py test_data/CurrentSPACsasofOctober2020.csv  test_data/octoberOCCnewoptionmarketunderlyings.csv
```

Test Usage:
```
pytest
```
