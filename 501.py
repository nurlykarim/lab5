import re

txt = input()
x = re.search("^Hello", txt)#re.match("Hello", txt)
if x:
  print("Yes")
else:
  print("No")
