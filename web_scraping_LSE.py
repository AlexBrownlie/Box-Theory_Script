######## TESTING WEB SCRAPING ########
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd
from selenium.webdriver.firefox.options import Options
# To download historical data
import wget

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Firefox("geckodriver-v0.25.0-linux64", firefox_options=options)

## Stores name, price and rating of products
acronyms=[]
names=[]
prices=[]
price_changes=[]
percent_changes=[]


## Sets URL to be scraped
driver.get("https://www.londonstockexchange.com/exchange/prices-and-markets/stocks/risers-and-fallers/risers-fallers.html")

content = driver.page_source
driver.quit()
soup = BeautifulSoup(content)

my_table=soup.find('table',{'class':'table_dati'})
#rows = my_table.findAll('a', attrs = {'class' : 'name'})
##for row in my_table.findAll('td', attrs = {'class':'name', 'scope':'row'}):
##    name = row.text
##    names.append(name)
##    #print(name)

i = 1
for row in my_table.findAll('td'):
    if (not row.text):
        continue
    elif (len(row.text) < 3):
        continue
    
    elif (i%5 == 0):
        percent_change = row.text
        percent_changes.append(percent_change)
        #print("% change" , row.text, "\n")
        i=0

    elif (i%4 == 0):
        price_change = row.text
        price_changes.append(price_change)
        #print("price change" , row.text, "\n")


    elif (i%3 == 0):
        price = row.text
        prices.append(price)
        #print("price" , row.text, "\n")

    elif (i%2 == 0):
        name = row.text
        names.append(name)
        #print("name" , row.text, "\n")

    else:
        acronym = row.text
        acronyms.append(acronym)
        #print("acronym", row.text, "\n")
        
    # increase index of i if the row is not blank
    i+=1

#print(acronyms)
#print(names)
#print(prices)


j=0
#Download historical data
for ac in acronyms:
    try:
        wget.download('https://query1.finance.yahoo.com/v7/finance/download/'+acronyms[j]+'.L?period1=1537524403&period2=1569060403&interval=1d&events=history&crumb=ET1PwQZnBhq','stock_history.csv')
    except:
        print("Error.")
    j+=1
    
# Table of Stocks info (Top 10 risers/fallers)

# Saving data to CSV
try:
    df = pd.DataFrame({'Acronym':acronyms,'Name':names,'Price':prices, 'Price Change':price_changes}) 
    df.to_csv('stocks.csv', index=False, encoding='utf-8')
except:
    print("Error occurred while generating CSV.")
