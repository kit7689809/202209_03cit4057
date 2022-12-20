import requests as req
import pandas as pd

url = (
    "https://api.hkma.gov.hk/public/market-data-and-statistics/"
    "daily-monetary-statistics/daily-figures-interbank-liquidity?offset=0"
) 

response = req.get(url)
resp_json = response.json()
records = resp_json["result"]["records"]

df = pd.DataFrame.from_dict(records)
df_hibor = df[["end_of_date", "hibor_overnight"]]

print("End")