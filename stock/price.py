import numpy as np
import pandas as pd
import requests
import math
import yfinance as yf
import matplotlib.pyplot as plt
from SmartApi.smartConnect import SmartConnect


url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"

d = requests.get(url).json()

token_df = pd.DataFrame.from_dict(d)
token_df['expiry'] = pd.to_datetime(token_df['expiry'])

token_df = token_df.astype({'strike': float})

# print(token_df)
token_df.to_csv(r'C:\Users\Rohit Anand\Desktop\coding\python\stock\instrument'+ 'angel_token.csv', header= True, index = False)


