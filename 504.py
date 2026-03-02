import re

txt = input()


digits = re.findall("[0-9]", txt)

for d in digits:
    print(d, end=" ")