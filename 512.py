import re

txt = input()


digits = re.findall(r"\d{2,}", txt)

for d in digits:
    print(d, end=" ")