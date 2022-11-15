import re

v = open('kakioko.txt')
t = v.readlines()
r = []

for i in range(len(t)):
    if re.match(r"\d+:\d+", t[i]):
        r.append(t[i].rstrip()+'\t')
    else:
        r.append(t[i])

z = ''.join(r)

with open('output.txt', mode='w') as f:
    f.write(z)
