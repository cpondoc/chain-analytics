# eth_tvl.py
# Getting Total Value Locked in Ethereum
# Tool Used: DeFi Llama (/tvl/Ethereum endpoint)

# Libraries
import requests
import matplotlib.pyplot as plt

# Grabbing data from DeFi Llama
response = requests.get("https://api.llama.fi/charts/Ethereum")
response_json = response.json()

# Timestamps and Liquidity
timestamps = []
liquidity = []

# Iterating through JSON
for item in response_json:
    timestamps.append(item['date'])
    liquidity.append(item['totalLiquidityUSD'])

# Setting up plot
fig, ax = plt.subplots()
ax.stem(timestamps, liquidity)

# Adjusting labels and checking
plt.xticks(color='w')
plt.xlabel("Time")
plt.ylabel("Total Value Locked ($)")
plt.title("Total Value Locked over Time in Ethereum")
plt.savefig('img/eth_tvl.png')