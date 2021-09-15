
#def linear(list1,n,key):
#    n=len(list1)
#    for i in range(0,n):
#        if key == list1[i]:
#            return i  
#    return -1
#
#list1=[12,32,23,10,45]
#key = 32
#n = len(list1)  
#res = linear(list1, n, key)  
#if(res == -1):  
#    print("Element not found")  
#else:  
#    print("Element found at index: ", res)

l=[1,2,3,4,5,6,7,8,9,10,11,12,13]
n=len(l)
key=input("Enter the key")
for i in range(0,n):
    if (l[i]==key):
        print("Number is present in the list")
    else:
        print("Number is not present in the list")