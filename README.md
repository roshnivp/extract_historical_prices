# Extract Historical Prices
 Python program to fetch the historical prices and dates of gold and silver from web

## Steps to Run:

1) Run scrapingGoldAndSilver (generates silver.csv which contains silver price data and gold.csv which contains gold price data)
      `python  scrapingGoldAndSilverData.py`
      
      
2) Run getCommodityPrice.py start_date(in the format 2017-05-10) end_date(in the format 2017-05-22) commodity
    ```sh
    $ ./getCommodityPrice.py 2017-08-25 2017-09-06 silver
    silver 17.56 0.1
     
    $ ./getCommodityPrice.py 2017-08-25 2017-09-06 gold
    gold 1326.12 200.91
    ```
      

##### Note: 
    1. There is no data for August 26,2017 in both websites
    2. Assuming python is present in /usr/bin/python
    3. To run scrapingGoldAndSliver you need pandas, lxml.html
            