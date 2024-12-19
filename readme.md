# Currency App

Convert currency based on exchange rate from a text file.


## How to run

```
python3 app.py
```

Load data
```
ACME(tm) US DOLLAR EXCHANGE RATE APP
1) LOAD currency exchange rate data from a file
2) USE AVERAGE exchange rate
3) USE HIGHEST exchange rate
4) USE LOWEST exchange rate
5) CONVERT USD TO EUR
6) CONVERT USD TO AUD
7) CONVERT USD TO GBP
0) QUIT program
Choose what to do: 1
Give name of the data file: currency.txt 
.
.
.
.
Data loaded successfully!
Currency exchange data is from 366 days between 1.1.2020
 and 31.12.2020 0.81493 1.295412        0.732646
```
Choose rate
```
ACME(tm) US DOLLAR EXCHANGE RATE APP
1) LOAD currency exchange rate data from a file
2) USE AVERAGE exchange rate
3) USE HIGHEST exchange rate
4) USE LOWEST exchange rate
5) CONVERT USD TO EUR
6) CONVERT USD TO AUD
7) CONVERT USD TO GBP
0) QUIT program
Choose what to do: 4
Using the lowest currency exchange rate.
```
Choose what to convert
```
ACME(tm) US DOLLAR EXCHANGE RATE APP
1) LOAD currency exchange rate data from a file
2) USE AVERAGE exchange rate
3) USE HIGHEST exchange rate
4) USE LOWEST exchange rate
5) CONVERT USD TO EUR
6) CONVERT USD TO AUD
7) CONVERT USD TO GBP
0) QUIT program
Choose what to do: 7
Give USD to convert: 777
777.0 USD in GBP is 569.27 GBP
```
Quit
```
ACME(tm) US DOLLAR EXCHANGE RATE APP
1) LOAD currency exchange rate data from a file
2) USE AVERAGE exchange rate
3) USE HIGHEST exchange rate
4) USE LOWEST exchange rate
5) CONVERT USD TO EUR
6) CONVERT USD TO AUD
7) CONVERT USD TO GBP
0) QUIT program
Choose what to do: 0
```

## Structure

```
currency/
    app.py
    currency.txt
    readme.md
```

## Coder

Laura Levistö
2021