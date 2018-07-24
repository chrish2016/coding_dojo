import pprint
n = 12
m = list(list(range(1*i,(n+1)*i, i)) for i in range(1,n+1))
pprint.pprint(m)