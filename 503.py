import re

txt = input()
pattern = input()


x = re.findall(pattern, txt)
print(len(x))