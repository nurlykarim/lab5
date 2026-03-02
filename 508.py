import re
s=input()
d=input()

part = re.split(d, s)
print(",".join(part))

