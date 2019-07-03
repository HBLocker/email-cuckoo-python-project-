#open file stream recersivly 
#as opened encrypt files 
#randome keys per time 
#done
import os
from cryptography.fernet import Fernet
 

path = 'c:\\projects\\hc2\\'

files = []
key = Fernet.generate_ley() #key making function
K_gen = Fernet(key) #pases key to func
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))
            

for f in files:
    token = k_gen.encrypt(f,'rb')
    token
    
    
    print(f)
