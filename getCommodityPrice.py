#!/usr/bin/python
import sys
import numpy as np

def getCommodityPrice(argv):

    start_date = argv[0]
    end_date = argv[1]
    commodity = argv[2]
    end_counter=0
    start_counter=0
    priceList=[]

    txtFile ="./formattedGold.txt" if commodity=='gold' else "./formattedSilver.txt"

    with open(txtFile, 'r') as inputFile:

        for line in inputFile:
            data = line.split(' ')
            if(data[0]!= end_date):
                end_counter = end_counter+1
            else:
                break

    with open(txtFile, 'r') as inputFile:
        for line in inputFile:
            data = line.split(' ')
            if(data[0]!= start_date):
                start_counter = start_counter+1
            else:
                break

    with open(txtFile, 'r') as inputFile:
        for i,line in enumerate(inputFile):
            data = line.split(' ')
            price = float(data[1].replace(',',''))

            if(i>=end_counter and i<= start_counter):
                #print(price)
                priceList.append(price)               # append price details within the start and end end date range
            elif(i>start_counter):
                break

    #print(end_counter)
    #print(start_counter)
    #print(len(priceList))
    mean = round(np.mean(priceList),2)         # calculating mean
    variance =round(np.var(priceList),2)       # calculating variance
    print(commodity+' '+str(mean)+' '+ str(variance))

if __name__ == "__main__":
   getCommodityPrice(sys.argv[1:])