import subprocess
import json
import os
import dotenv

from constants import *

dotenv.load_dotenv()

mnemonic = os.getenv("mnemonic", "mnemonic")

command = './derive -g --mnemonic=mnemonmic --cols=path,address,privkey,pubkey --numderive=12 --format=json --coin'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)
