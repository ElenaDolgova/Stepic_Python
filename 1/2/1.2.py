ans = 0
k=0
objects = [1, 2, 1, 2, 3]
d=[]
for obj in objects:
    if obj not in d:
        d.append(obj)
print(len(d))