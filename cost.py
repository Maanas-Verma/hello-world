import numpy as np
def j(o0,o1):
    n=0
    for i in g:
        n+=(o0+(o1*i[0])-i[1])**2.0
    return n/(len(g)*2.0)    
def j0(o0,o1):
    n=0
    for i in g:
        n+=(o0+(o1*i[0])-i[1])*2.0
    return n/(len(g)*2.0)
def j1(o0,o1):
    n=0
    for i in g:
        n+=(o0+(o1*i[0])-i[1])*2.0*i[0]
    return n/(len(g)*2.0)

p=open('test0','r')
l=input('tell no of input taken')
g=[]
for i in range(int(l)):
    r=p.readline().split(' ')
    r[0]=int(r[0])
    r[1]=int(r[1][:(len(r[1])-1)])
    g.append(r)
p.close()
print(g)

o0=0
o1=0
b=5
a=0.1
f=0
while(abs(b)<10000000):
    from0=o0-a*j0(o0,o1)
    from1=o1-a*j1(o0,o1)
    o0=from0
    o1=from1
    b=j0(o0,o1)+j1(o0,o1)
    f+=1
    print('the procedue is caring ',f,'and value of b is ',b)
print(o0,o1)
print(o0+o1*float(input('type value of x :')))
print(f)
