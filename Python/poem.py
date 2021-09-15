f=open('poem.txt')
t=f.read()
if 'twinkle' in t:
    print("It is present")
else:
    print("It is not present")
f.close()