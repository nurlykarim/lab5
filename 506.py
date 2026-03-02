import re

txt = input()

x = re.search(r"[^ ]+@[^ ]+\.[^ ]+", txt)
if x:
    print(x.group())
else:
    print("No email")