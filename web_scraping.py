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
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")

content = driver.page_source
soup = BeautifulSoup(content)
def main():
    # Finding everything that is in this class
    for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
        name=a.find('div', attrs={'class':'_3wU53n'})
        price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
        rating=a.find('div', attrs={'class':'hGSR34'})

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
            
        try:
            ratings.append(rating.text)
        except:
            ratings.append("empty")
            

    # Saving data to CSV
    df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
    df.to_csv('products.csv', index=False, encoding='utf-8')

    
main()
