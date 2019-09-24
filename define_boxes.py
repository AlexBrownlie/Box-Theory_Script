######### Defining the Darvas boxes #########
## For practice maybe use data from 8 weeks ago so can run algorithm on last
## 4 weeks and see how it would have acted (when it buys/sells etc and if it
## would have made any profit)
import csv

## Get a list of previous stock prices [given an array of acronyms]
def get_box(stock):
    ## For the moment just use predownloaded history. Tried multiple ways of downloading
    ## url and none have worked.
    #url = "http://query1.finance.yahoo.com/v7/finance/download/{}.L?period1=1537693886&period2=1569229886&interval=1d&events=history&crumb=Fvb/I2/T6oO".format(stock)
    with open("stock_files/{}.L.csv".format(stock), "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        dates=[]
        closes=[]
        volumes=[]

        i=0
        for row in csv_reader:
            if ('null' not in row) and (i!=0):
                dates.append(row[0])
                closes.append(row[4])
                volumes.append(row[6])
            i+=1
    #print len(dates)
    #print len(closes)
    #print len(volumes)

    # Maybe get rid of last 4 weeks worth for testing?
    # Or percentage e.g. remove 25% of results

    
    ## Find the 52 week high? Set this as bottom of box?
    high = max(closes)
    # May not work if same value has been the high multiple times
    high_index = closes.index(high)
    print(high)
    print(high_index)

    ########## OR ##########

    ## Find the 4 week high - find range of values since then
    ## If its been bouncing around the same values for 4 weeks then set the
    ## max value as the lower limit of the box.


## Find the volume traded


stocks=["ASAI", "RDI", "PURE", "RAV", "JUST"]

## FOR LOOP once function tested
for stock in stocks:
    get_box(stock)


