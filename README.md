# Ethereum Block Fetcher

A simple Python script to fetch the latest Ethereum block from public RPC endpoints and display the block information.

## Usage

```bash
python fetch_eth_block.py
```

## Features

- Fetches the latest Ethereum block from multiple public RPC endpoints
- Displays key block information including:
  - Block number
  - Block hash
  - Timestamp
  - Number of transactions
  - Gas used
  - Gas limit
  - Miner/validator address
  - Parent hash

## Requirements

- Python 3.6+
- Requests library (`pip install requests`)
