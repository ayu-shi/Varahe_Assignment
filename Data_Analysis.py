import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class DataAnalysis:
  def prepareData(self):
    try:
        readData = pd.read_csv('C:\\Users\\sharm\\cryptoData.csv')
    except IOError as e:
        raise e
    readData["4"] = pd.to_numeric(readData["4"], downcast="float")
    readData["3"] = pd.to_numeric(readData["3"], downcast="float")
    resultsPerCoin = readData.groupby('5').head(30)
    top30ResultsPerCoin = readData.groupby('5').head(30)
    return top30ResultsPerCoin, resultsPerCoin

  def bitcoinAnalysis(self, data):
    print("-------- BITCOIN ANALYSIS --------\n")
    print("******* Average of Bitcoin for last 30 Days *******")
    print((data.groupby('5')['4'].mean()).loc['bitcoin'])

    print()
    print("******* Standard Deviation of Bitcoin for last 30 Days *******")
    print((data.groupby('5')['4'].std()).loc['bitcoin'])

    print()
    print("******* Minimum of Bitcoin for last 30 Days *******")
    print((data.groupby('5')['4'].min()).loc['bitcoin'])

    print()
    print("******* Maximum of Bitcoin for last 30 Days *******")
    print((data.groupby('5')['4'].max()).loc['bitcoin'])

    print()
    print("******* Median of Bitcoin for last 30 Days *******")
    print((data.groupby('5')['4'].median()).loc['bitcoin'])

  def ethereumAnalysis(self, data):
    print("\n-------- ETHEREUM ANALYSIS --------\n")
    print("******* Average of Ethereum for last 30 Days *******")
    print((data.groupby('5')['4'].mean()).loc['ethereum'])

    print()
    print("******* Standard Deviation of Ethereum for last 30 Days *******")
    print((data.groupby('5')['4'].std()).loc['ethereum'])

    print()
    print("******* Minimum of Ethereum for last 30 Days *******")
    print((data.groupby('5')['4'].min()).loc['ethereum'])

    print()
    print("******* Maximum of Ethereum for last 30 Days *******")
    print((data.groupby('5')['4'].max()).loc['ethereum'])

    print()
    print("******* Median of Ethereum for last 30 Days *******")
    print((data.groupby('5')['4'].median()).loc['ethereum'])

  def correlationBitcoinAnalysis(self, data):
    print("\n-------- Bitcoin OC Correlation ANALYSIS --------\n")
    bitcoinData = (data[data['5'] == 'bitcoin'])
    print(bitcoinData['3'].corr(bitcoinData['4']))

  def correlationEthereumAnalysis(self, data):
    print("\n-------- Ethereum OC Correlation ANALYSIS --------\n")
    ethereumData = (data[data['5'] == 'ethereum'])
    print(ethereumData['3'].corr(ethereumData['4']))

  def getData(self, coin):
    try:
        readData = pd.read_csv('C:\\Users\\sharm\\cryptoData.csv')
    except IOError as e:
        raise e
    data = (readData[readData['5'] == coin])
    return data

  def findOutlier(self):
    print("\n-------- BITCOIN OUTLIER ANALYSIS --------\n")
    data = self.getData('bitcoin')
    sns.boxplot(data['4'])
    plt.show()
    print("Please refer BOXPLOT Generated")

  def findPatternBitcoinData(self):
    print("\n-------- Pattern ANALYSIS --------\n")
    data = self.getData('bitcoin')
    sns.lineplot(data['4'])
    plt.show()
    print("Please refer LINEPLOT Generated")
    
  def volumeChangeBitcoinEthereumData(self):
    print("\n-------- Volume ANALYSIS for Bitcoin and Ethereum for Lats 30 Days --------\n")
    dataBitcoin = self.getData('bitcoin')
    dataEthereum = self.getData('ethereum')
    volumeBitcoin = dataBitcoin.head(30)
    volumeEthereum = dataEthereum.head(30)
    s1=volumeBitcoin['2']
    s2=volumeEthereum['2']
    ax = s1.plot(x='2')
    s2.plot(ax=ax, x='2')
    plt.show()
    print("Please refer LINEPLOT Generated")

