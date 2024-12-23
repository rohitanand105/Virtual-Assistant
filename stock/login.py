import numpy as np
import pandas as pd
import requests
import math
import yfinance as yf
import matplotlib.pyplot as plt
from SmartApi.smartConnect import SmartConnect

# Banknifty = yf.download("^NSEBANK", start = "2023-09-15", end = "2023-09-16")

# print(Banknifty.loc[:,"Close"])



api_key = 'Er6rzIv4'
clientId = 'Your Client Id'
pwd = 'Your Pin'
smartApi = SmartConnect(api_key)
token = "Your QR code value"
totp=pyotp.TOTP(token).now()
correlation_id = "abc123"












