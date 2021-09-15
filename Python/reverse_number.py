t=int(input("Enter the number of test cases"))
for  i in range(0,t):
    n=int(input("Enter the number\n"))
    rev=0
    while n>0:
        ld=n%10
        rev=(rev*10)+ld
        n=n/10
    print(rev)