# eth_data.py
# Getting Block Size and Gas Used for Ethereum
# Tool Used: Alchemy (Ethereum API)

# Pertinent libraries
from web3 import Web3
import matplotlib.pyplot as plt

# Making connection to API usin
url = "https://eth-mainnet.alchemyapi.io/v2/siHtlzEkQN6a1GOnA1WYAXXF3Ep7IYjo"
web3 = Web3(Web3.HTTPProvider(url))

# Attributes wanted
sizes = []
block_nums = []
gas_used = []

# Get latest block
latest_block = web3.eth.get_block('latest')
block_number = latest_block['number']
block_nums.append(block_number)
sizes.append(latest_block['size'])
gas_used.append(latest_block['gasUsed'])

# Get all block sizes for a certain range
for i in range(1, 100):
    current_block = web3.eth.get_block(block_number - i)
    sizes.append(current_block['size'])
    block_nums.append(current_block['number'])
    gas_used.append(current_block['gasUsed'])

# Reverse block nums and sizes
sizes = sizes[::-1]
block_nums = block_nums[::-1]
gas_used = gas_used[::-1]

# Plot figure of block sizes
fig, ax = plt.subplots()
ax.stem(block_nums, sizes)

# Configure plot
plt.xlabel("Block Number")
plt.ylabel("Block Size")
plt.title("Block Size over time in Ethereum")
plt.savefig('./img/eth_block_size.png')

# Plot figure of gas
fig, ax = plt.subplots()
ax.stem(block_nums, gas_used)

# Configure plot
plt.xlabel("Block Number")
plt.ylabel("Gas Used")
plt.title("Gas Used per Block over time in Ethereum")
plt.savefig('./img/eth_gas_used.png')