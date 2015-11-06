#one key have many values
from collections import defaultdict

d = defaultdict(list)
b = defaultdict(set)

d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['a'].append(2)

b['a'].add(1)
b['a'].add(2)
b['a'].add(3)
b['a'].add(2)

print(d)
print(b)