t=int(input("Enter number of test cases\n"))
for i in range(1,t+1):
    n=int(input("Enter the number"))
    f=1
    for j in range(1,n+1): 
        f=f*j
    print(f)
    