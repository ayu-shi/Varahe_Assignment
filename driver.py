from Scrapping_Data import Scrape
from Data_Analysis import DataAnalysis
from uploadToCloud import Upload
import os
import pathlib

print("=====READING AND PREPARING DATASET IN PROGRESS=====\n")
coins = ["bitcoin", "ethereum", "tether", "bnb", "cardano"]
tables = []
scrapeObj = Scrape(coins, tables)
data = scrapeObj.fetchPrepareData()
scrapeObj.prepareCSV(data)
print("\n=====READING AND PREPARING DATASET COMPLETED=====\n")

print("\n=====DATA ANALYSIS IN PROGRESS=====\n")
DataAnalysisObj = DataAnalysis()
Data, allData = DataAnalysisObj.prepareData()

DataAnalysisObj.bitcoinAnalysis(Data)
DataAnalysisObj.ethereumAnalysis(Data)

DataAnalysisObj.correlationBitcoinAnalysis(Data)
DataAnalysisObj.correlationEthereumAnalysis(Data)

DataAnalysisObj.findOutlier()
DataAnalysisObj.findPatternBitcoinData()
DataAnalysisObj.volumeChangeBitcoinEthereumData()
print("\n=====DATA ANALYSIS COMPLETED=====\n")

print("\n=====UPLOADING FILE TO AWS S3 IN PROGRESS=====\n")
bucket_name = "varaheassignment"
object_name = "data.csv"
file_name = os.path.join(pathlib.Path(__file__).parent.resolve(), "cryptoData.csv")
uploadObj = Upload(bucket_name, object_name, file_name)
uploadObj.uploadFile()
print("\n=====UPLOADING FILE TO AWS S3 COMPLETED=====\n\n")

