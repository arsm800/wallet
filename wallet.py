import subprocess
import json
import os
import dotenv

from constants import *

dotenv.load_dotenv()

mnemonic = os.getenv("MNEMONIC", "mnemonic")

command = './derive -g --mnemonic="sunny carpet addict journey solid noodle grab exercise limb puppy process diary" --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)
