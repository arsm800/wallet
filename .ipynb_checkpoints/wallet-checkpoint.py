# Imports
import subprocess
import json
import os
import dotenv

from constants import *

dotenv.load_dotenv()

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
    
derive_wallets()
