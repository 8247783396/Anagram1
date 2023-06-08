a=input().split()
a=set(a)
d={}
for i in a:
    s=sorted(i)
    k="".join(s)
    if k not in d:
        d[k]=[i]
    else:
        d[k].append(i)
print(list(d.values()))