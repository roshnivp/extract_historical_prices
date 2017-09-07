import lxml.html as LH
import requests
import pandas as pd
import csv
from dateutil.parser import parse

# function to change date format from "Sep 07, 2017" to "2017-09-07"
def changeDateFormat(sourceFile, destFile):
    with open(sourceFile, 'r') as csvfile, open(destFile, 'w') as temp_file:
        r = csv.reader(csvfile)
        next(r, None)
        for row in r:
            dt = row[0]
            dt = parse(dt)
            current_dt = dt.strftime('%Y-%m-%d')
            row[1] = row[1].replace(',', '')
            temp_file.write(current_dt + ' ' + row[1] + '\n')

def text(elt):
    return elt.text_content().replace(u'\xa0', u' ')


def extractAndStoreData(url):
    header_info = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5)"}
    output_file = "gold.csv" if ("gold" in url) else "silver.csv"
    response = requests.get(url, headers=header_info)
    content = LH.fromstring(response.content)

    for table in content.xpath('//*[@id="curr_table"]'):
        col = [text(th) for th in table.xpath('//*[@id="curr_table"]//th')]  # find the columns
        data = [[text(td) for td in tr.xpath('td')]
                for tr in table.xpath('//*[@id="curr_table"]//tr')]  # returns each row
        data = [row for row in data if len(row) == len(col)]  # filter out invalid rows
        data = pd.DataFrame(data, columns=col)  # converting to table

        gold_data = data[['Date', 'Price']]
        gold_data.to_csv(output_file, index=False, encoding='utf-8')  # writing data to file

# extracting historical prices and dates of gold
extractAndStoreData('https://www.investing.com/commodities/gold-historical-data')
changeDateFormat("gold.csv", "formattedGold.txt")


# extracting historical prices and dates of silver
extractAndStoreData('https://www.investing.com/commodities/silver-historical-data')
changeDateFormat("silver.csv", "formattedSilver.txt")

