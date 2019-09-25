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
            if ('null' not in row) and (i > 0):
                dates.append(row[0])
                closes.append(row[4])
                volumes.append(row[6])
            i+=1
    #print len(dates)
    #print len(closes)
    #print len(volumes)

    #high = fiftytwo_wh(closes)
    #print(high)
    
    ########## OR ##########
    ## Find the 4 week high - find range of values since then
    
    # remove the most recent 4 weeks (for testing purposes)
    n=20
    closes = closes[:len(closes)-n]
    dates = dates[:len(dates)-n]
    volumes = volumes[:len(volumes)-n]

    # Only use the most recent 4 weeks to determine performance
    n = len(closes)-20
    del closes[:n]
    del dates[:n]
    del volumes[:n]

    #variation = float(max(closes)) - float(min(closes))
    #print(str(variation))

    
    ## If its been bouncing around the same values for 4 weeks then set the
    ## max value as the lower limit of the box - if it goes above this then buy.
    
    ## Checks if the price has gone over the max from the last 4 weeks
    ## Get the minimum from that period
    minimum = float(min(closes))
    maximum = float(max(closes))
    ## Find how many times its passed the midpoint
    price_range = maximum - minimum
    midpoint = maximum - (price_range/2)
    print(midpoint)

    ## Check how many times the price crossed the midpoint
    ## (point n < midpoint, point n+1 > midpoint)

    
    ## and which direction it was going in.

def fiftytwo_wh(closes):
    ## Find the 52 week high? Set this as bottom of box?
    high = max(closes)
    # May not work if same value has been the high multiple times
    #high_index = closes.index(high)
    
    return(high)

    
## Find the volume traded



stocks=["ASAI", "RDI", "PURE", "RAV", "JUST"]

## FOR LOOP once function tested
for stock in stocks:
    get_box(stock)
