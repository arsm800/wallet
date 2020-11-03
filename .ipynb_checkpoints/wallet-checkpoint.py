import subprocess
import json
from constants import *

command = './derive -g --mnemonic="sunny carpet addict journey solid noodle grab exercise limb puppy process diary" --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)
