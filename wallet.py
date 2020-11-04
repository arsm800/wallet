# Imports
import subprocess
import json
import os
import dotenv

from constants import *
from bit import PrivateKeyTestnet
from eth_account import Account
from web3 import Web3

dotenv.load_dotenv()

w3=Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Mnemonic variable for cryptowallet private key stored in .env file
mnemonic = os.getenv("mnemonic", "mnemonic")

# Establish variable for derive command 
command = './derive -g --mnemonic=mnemonmic --cols=path,address,privkey,pubkey --numderive=12 --format=json --coin'

# Create function to derive wallets
def derive_wallets():

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()

    keys = json.loads(output)
    
    # Create dictionary to assign 4 keys to each currency created in constants.py
    coins = {
             BTC: [keys[0], keys[1], keys[2], keys[3]],
             ETH: [keys[4], keys[5], keys[6], keys[7]],
             BTCTEST: [keys[8], keys[9], keys[10], keys[11]]
            }
    
    print(coins)
    print(coins[ETH][2]['privkey'])
    
    return(coins)
    
    # Test query
    #print(coins[ETH][2]['privkey'])





# print(derive_wallets()[ETH])

# Create function to convert private key string to an account object usable in bit or web3
def privkey_to_account(coin, privkey):
    
    if coin == ETH:
        return Account.privateKeyToAccount(privkey)
    
    elif coin == BTCTEST:
        return PrivateKeyTestnet(privkey)



# Create function to create raw, unsigned transaction
def create_tx(coin, account, to, amount):
    
    if coin == ETH:
        
        gasEstimate = w3.eth.estimateGas({"from": account.address, 
                                      "to": to, 
                                      "value": amount})
        
        return {"from": account.address, 
                "to": to, 
                "value": amount, 
                "gasPrice": w3.eth.gasPrice, 
                "gas": gasEstimate, 
                "nonce": w3.eth.getTransactionCount(account.address)}
    
    elif coin == BTCTEST:
        PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])


# Create function to sign transaction and send to designated network
def send_tx(coin, account, to, amount):
    pass
    

    
    
    
    
# Try out functions    
derive_wallets()
privkey_to_account(ETH, "KzuAJjV8NhvAraszwBtANcKhy5i7npNHhKZB9mSq9oMbPuAAGYoC")