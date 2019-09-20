######## TESTING WEB SCRAPING ########
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

driver = webdriver.Firefox("geckodriver-v0.25.0-linux64")

## Stores name, price and rating of products
products=[]
prices=[]
ratings=[]
## Sets URL to be scraped
driver.get("https://www.londonstockexchange.com/exchange/prices-and-markets/stocks/risers-and-fallers/risers-fallers.html")

content = driver.page_source
soup = BeautifulSoup(content)
def main():
    # Finding everything that is in this class
    for a in soup.findAll('a',href=True, attrs={'class':'column1_nomenu'}):
        name=a.find('div', attrs={'class':'name'})
        price=a.find('div', attrs={'class':'price'})

        ## Try except loops so that it can be seen where incorrect classes
        ## are given - will return "empty" in CSV.
        try:
            products.append(name.text)
        except:
            products.append("empty")
            
        try:
            prices.append(price.text)
        except:
            prices.append("empty")
            

    # Saving data to CSV
    df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
    df.to_csv('stocks.csv', index=False, encoding='utf-8')

    
main()

