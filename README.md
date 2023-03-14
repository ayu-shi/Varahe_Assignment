# Varahe_Assignment

Install libraries beautifulsoup4, requests, pandas, numpy, seaborn, matplotlib.pyplot

download all the .py files from the repo

Run the driver.py file
The output will be consisting of running the scrapper, analysis and data storage to cloud.

below are the screenshots for all the tasks that driver.py will do.

![scrapping](https://user-images.githubusercontent.com/47883106/224790356-d0ed64cd-5048-428a-919d-1e3db2bc8e8c.png)

Above screenshot is from scrapping data and will be scrapping data and preparing it and finally prepare csv dataset out of it.

![bitcoin_analysis](https://user-images.githubusercontent.com/47883106/224790462-ae831cef-ed16-4210-bd8f-1f1f6fe0bbd0.png)

Above screenshot shows the analysis on Bitcoin data for last 30 days.

![ethereum_analysis](https://user-images.githubusercontent.com/47883106/224790480-5a491b57-1e5c-4dd8-8e34-165b7cd3c227.png)

Above screenshot shows the analysis on Ethereum data for last 30 days.

![correlation](https://user-images.githubusercontent.com/47883106/224790504-3acd29ef-a538-4f6d-88cc-a90c369d4d80.png)

Above screenshot shows the correlation on Bitcoin open/close data and Ethereum open/close data. 

![outlier](https://user-images.githubusercontent.com/47883106/224790571-ae7d3076-6e0f-48e8-8956-0f10fbcaddb7.png)

Above screenshot shows the boxplot that clearly shows the outliers below the lower line and they are outliers because these values lies outside of the most of the other values in the Bitcoin data.

![patterns](https://user-images.githubusercontent.com/47883106/224790607-8cf7af58-419f-482f-84d2-b07d8d5e9bd6.png)

Above screenshot shows the Bitcoin data in Line graph that clearly shows the downtrend pattern because the data values are continuously getting reduced.

![volume](https://user-images.githubusercontent.com/47883106/224790636-dc66d447-9d8b-4846-915e-064e51ad8e32.png)

Above screenshot shows the volume for Bitcoin and Ethereum for last 30 days. Is there any pattern? Yes the volume graph is like a channel thats shows volumes in both the currencies in last 30 days are not going above the top value and not going below the bottom value.

![charts](https://user-images.githubusercontent.com/47883106/224790666-e227baf5-8917-4353-b708-c18c8ed536f9.png)

Above screenshot shows the outlier, volume, pattern analysis that has to be done using plots above.

![data_uploading](https://user-images.githubusercontent.com/47883106/224790716-1f65e940-03e7-4387-8a97-bc03151cb524.png)

Above screenshot shows the dataset uploaded to AWS cloud s3
When you run the driver.py this may not work for you as I have done it with IAM user created locally, so attaching screenshot of file uploaded to s3 as well below!

![dataoncloud](https://user-images.githubusercontent.com/47883106/224940468-e6fd4dea-3d1f-455a-874b-1ba4fb8d0880.png)


