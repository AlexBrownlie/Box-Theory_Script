######## TESTING WEB SCRAPING ########
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

driver = webdriver.Firefox("geckodriver-v0.25.0-linux64")

## Stores name, price and rating of products
stocks=[]

## Sets URL to be scraped
driver.get("https://www.londonstockexchange.com/exchange/prices-and-markets/stocks/risers-and-fallers/risers-fallers.html")

content = driver.page_source
soup = BeautifulSoup(content)

my_table=soup.find('table',{'class':'table_dati'})
#rows = my_table.findAll('a', attrs = {'class' : 'name'})
for row in my_table.findAll('td', attrs = {'class':'name'}):
    stock = row.
    stocks.append(stock)
    print(stock)
# Table of Stocks info (Top 10 risers/fallers)
#print(stocks)


# Saving data to CSV
#df = pd.DataFrame({'Product Name':products,'Price':prices}) 
#df.to_csv('stocks.csv', index=False, encoding='utf-8')

    

