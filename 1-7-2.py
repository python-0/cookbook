#dict must be order
from collections import OrderedDict

d = OrderedDict()
b={}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

b['a'] = 1
b['b'] = 2
b['c'] = 3
b['d'] = 4


import json
print(json.dumps(b)) # {"a": 1, "c": 3, "b": 2, "d": 4}
print(json.dumps(d)) # {"a": 1, "b": 2, "c": 3, "d": 4}
