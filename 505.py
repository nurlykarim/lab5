import re

txt = input()
x = re.search("^[a-zA-Z].*[0-9]$", txt)
if x:
  print("Yes")
else:
  print("No")
