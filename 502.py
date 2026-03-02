import re

txts = input()
txtp = input()

if re.search(txtp, txts):
    print("Yes")
else:
    print("No")