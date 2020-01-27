# Bitcoin_price_predict_BIG_DATA
Developed an end to end pipeline in GCP to estimate bitcoin price. Web scrapped Streaming data and Implemented ARIMA model using mapper reducers. Designed a tableau dashboard for real time monitoring as end product of pipeline

Steps to Reproduce:
1. Download historical data of bitcoin prices from Kaggle: https://www.kaggle.com/mczielinski/bitcoin-historical-data
2. Split the historical data into train and test data and pass the data through team1_arima.py
3. Run the scraper code team1_scraper.ipnyb to get streaming data and store the streaming data in a csv file
4. Load the CSV file in the scraper code and log transform the prices to avoid abnormalities and to make data stationary
5. Export the data to a txt file.
6. Load the txt file generated in Hue environment and pass it through mapper and reducer which will give us the predicted values given by the ARIMA equation. The reducer gives a key value pair of timestamp and predicted prices.
7. The output from the mapred streaming is then fed into Hive and in the database a table is created using the output.
8. Run queries in Hive


Youtube Link for video: https://youtu.be/IbAFWoDOaSM
