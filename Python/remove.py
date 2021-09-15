def remove(word,string):
    newstr=string.replace(word,"")
    return newstr.strip()

str=input("Enter the string")
wr=input("Ente the number to be replaced")
print(remove(wr,str))