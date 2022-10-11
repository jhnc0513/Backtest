import requests
import pandas as pd

r = requests.get("https://ftx.com/api/markets")
df = pd.DataFrame(r.json()['result'])
df.index = df.name
spot_df = df[df.type == 'spot']  # dataframe with only spot
spot_df = spot_df[spot_df.tokenizedEquity.isna()]  # Filter out tokenized stocks
spot_df = spot_df[spot_df.isEtfMarket == False]
spot_df = spot_df[spot_df.quoteCurrency == 'USD']
# spot_df_sort = spot_df.change1h.sort_values(ascending=False)

spot_df_sort = spot_df.change1h.sort_values(ascending=False).head(10)
print(spot_df_sort)

# What are the realtime movements?
# a set of cryptos, for instance eth, btc, gmx
# which one is moving the fastest
# build a websocket stream of multiple coins -> store it somewhere
# Database/csv -> keep track of the performance

