def reverse(str):
    str1=""
    for i in str:
        str1=i+str1
    return str1

str=input("Enter the string\n")
reversestr=reverse(str)
print(f"Reversed String is {reversestr}")
if reversestr == str:
    print("String is Palindrome")
else :
    print("String is not palindrome")