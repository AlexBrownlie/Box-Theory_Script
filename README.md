**INFO FOR HOME DEV**
Python libraries required: Selenium, BeautifulSoup, pandas, certifi, urllib3[secure]
[Pip install ...]

# geckodriver should be in this repo, following command needed for it to work.
export PATH=$PATH:/path/to/directory/of/executable/

# Box-Theory_Script
This project will be implementing Darvas' Box Theory, used to determine when to buy/sell certain stocks.
It will be written in Python and will use data scraping to find the best stocks to use and when it should buy/sell them.
Uses end of day stocks and compares the days to make boxes. To start with it will scrape data from exchange for the past [12 months?] to find the [52?] week high [and low?]

**Possible Future Additions**
Implement machine learning so that the program learns from its mistakes.
Use pyplot or similar so that physical graphs/boxes can be seen.
Connect to a stock exchange website so that it can automatically buy/sell, rather than having to wait until the user does it.
*Implement other theories*
Research other theories on the stock market. Implement them all together (possible based off weighting) to determine buy/sell rather than just one theory.

**Instructions** 
Once a base script has been completed, instructions for how to setup/run this script will be inserted here.
