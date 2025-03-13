#!/usr/bin/env python3
import json
import requests
from datetime import datetime

# List of public Ethereum RPC endpoints
RPC_ENDPOINTS = [
    "https://eth.llamarpc.com",
    "https://ethereum.publicnode.com",
    "https://rpc.ankr.com/eth"
]

def fetch_latest_block(rpc_url):
    """Fetch the latest Ethereum block from the given RPC endpoint."""
    headers = {'Content-Type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": ["latest", True],
        "id": 1
    }
    
    try:
        response = requests.post(rpc_url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching from {rpc_url}: {e}")
        return None

def main():
    """Main function to fetch and display the latest Ethereum block."""
    print("Fetching latest Ethereum block...")
    
    # Try each endpoint until we get a successful response
    result = None
    for endpoint in RPC_ENDPOINTS:
        print(f"Trying endpoint: {endpoint}")
        result = fetch_latest_block(endpoint)
        if result and 'result' in result:
            break
    
    if not result or 'result' not in result:
        print("Failed to fetch the latest block from any endpoint.")
        return
    
    block = result['result']
    
    # Convert hex values to decimal where appropriate
    block_number = int(block['number'], 16)
    timestamp = int(block['timestamp'], 16)
    gas_used = int(block['gasUsed'], 16)
    gas_limit = int(block['gasLimit'], 16)
    
    # Format timestamp
    timestamp_str = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S UTC')
    
    # Print block information
    print("\n===== LATEST ETHEREUM BLOCK =====")
    print(f"Block Number: {block_number}")
    print(f"Block Hash: {block['hash']}")
    print(f"Timestamp: {timestamp_str}")
    print(f"Transactions: {len(block['transactions'])}")
    print(f"Gas Used: {gas_used:,}")
    print(f"Gas Limit: {gas_limit:,}")
    print(f"Miner/Validator: {block['miner']}")
    print(f"Parent Hash: {block['parentHash']}")
    print("=================================\n")

if __name__ == "__main__":
    main()
