y={'sarojith':20,'jerome':10,'arjun':5,'vishnu':1}
l=list(y.items())
l.sort()
print('Ascending order is',l)
l=list(y.items())
l.sort(reverse=True)
print('Descending order is',l)
dict=dict(l)
