with open('sample.txt', 'r') as f:
    a=f.read()
print(a)

with open('sample.txt', 'w') as f:
    b=f.write("Sunbeam School")
print(b)