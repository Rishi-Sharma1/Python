s=input()
l={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
sumx=0

for i in range(len(l)-1):
    if(l[i[0]]<l[i+1[0]]):
        sumx-=l[i[0]]
    else:
        sumx+=l[i[0]]
print(sum)    