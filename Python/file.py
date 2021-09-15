#f=open('sample.txt','r')
f=open('sample.txt')
data=f.read(5) #reads first five character of file
print(data)
f.close()