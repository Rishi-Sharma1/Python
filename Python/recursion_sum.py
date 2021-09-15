def sum(a):
    s=0
    for i in range(0,a):
        s=sum(a-1)+a
    return s

n=int(input("Enter the number"))
print(sum(n))