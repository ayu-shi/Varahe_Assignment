from bs4 import BeautifulSoup
import requests
import pandas as pd

class Scrape:
  def __init__(self, coins, table):
    self.coins = coins
    self.tables = table

  def fetchPrepareData(self):
    for i in range(len(self.coins)):
        print("Processing Data for Coin {0}".format(self.coins[i]))
        url = f'https://www.coingecko.com/en/coins/{self.coins[i]}/historical_data?start_date=2023-01-01&end_date=2023-02-28'
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:  
            raise SystemExit(e)
        soup = BeautifulSoup(response.content, 'html.parser')
        df = pd.read_html(str(soup))[0]
        df = df.dropna()
        l = df.values.tolist()
        for k in range(len(l)):
            l[k].append(self.coins[i])
        for p in range(len(l)):
            for q in range(len(l[p])):
                if "$" in l[p][q]:
                    s = (l[p][q]).replace(',','')
                    l[p][q] = s[1:]
        self.tables.append(pd.DataFrame(l))
    return self.tables

  def prepareCSV(self, data):
      master_table = pd.concat(data)
      df = pd.DataFrame(master_table)
      try: 
         master_table.to_csv("cryptoData.csv", index = False)
      except IOError as e:
         raise e
'''
coins = ["bitcoin", "ethereum", "tether", "bnb", "cardano"]
tables = []

scrapeObj = Scrape(coins, tables)
data = scrapeObj.fetchPrepareData()
scrapeObj.prepareCSV(data)
'''




