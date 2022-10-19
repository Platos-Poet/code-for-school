# This code recursivley extracts a nested zip file with an incrementing name
# and an incrementing password

# imports the ZipFile library
from zipfile import ZipFile

# Initializes the variables used for this file
i = 1
n = 1
p = 1

# a 
while i == 1:
   # Turn the formatted string for the password into bits
   mystring = f'LTSEC{n}'
   b = mystring.encode('utf-8')
# Create a ZipFile Object and load hmm{n}.zip in it
   with ZipFile(f'hmm{p}.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory with the password b in bytes
      zipObj.extractall(pwd = b)
      # Increments the variable for the loop
      p += 1
      n += 1
