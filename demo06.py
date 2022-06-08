
q = {'a':1,'b':2,'c':3}
w = {'d':4,'e':5}

print("通过键名获取:",q['a'])
q['f'] = 6
print(q)
r = q.fromkeys(['a','b'])
print(r)
print(q.get('w'))
print('a' in q)
q1 = q.items()
print(q1)
print(q.keys())
print(q.setdefault('g'))
print(q)
q.update({'j': '55'})
print(q)
print(q.values())
print(q.pop('a'))
print(q.popitem())