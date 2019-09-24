######### Defining the Darvas boxes #########
## For practice maybe use data from 8 weeks ago so can run algorithm on last
## 4 weeks and see how it would have acted (when it buys/sells etc and if it
## would have made any profit)
import requests
import os

import urllib.request

## Get a list of previous stock prices [given an array of acronyms]
def get_box(stock):
    url = "http://query1.finance.yahoo.com/v7/finance/download/{}.L?period1=1537693886&period2=1569229886&interval=1d&events=history&crumb=Fvb/I2/T6oO".format(stock)
    #print(url)
    try:
        response = requests.get(url)
        with open(os.path.join("stock_files", stock), "wb") as f:
            f.write(response.content)

        #stock_data = response.read()
        #with open(, 'wb') as f:
                  #f.write(stock_data)
    except:
        print("Did not work.\n")
    
    
    #open("stock_files/{}".format(stock), 'wb').write(stock_file.content)

    #print url
    


## Find the 52 week high? Set this as bottom of box?

## OR

## Find the 4 week high - find range of values since then
## If its been bouncing around the same values for 4 weeks then set the
## max value as the lower limit of the box.


## Find the volume traded


stocks=["ASAI", "RDI", "PURE", "RAV", "JUST"]

## FOR LOOP once function tested
for stock in stocks:
    get_box(stock)


