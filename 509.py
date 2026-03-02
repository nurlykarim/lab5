import re
s=input()
pattern = r'\b\w{3}\b'
found = re.findall(pattern, s)
print(len(found))
