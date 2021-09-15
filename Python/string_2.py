str='''Dear <|NAME|>, 
you are selected !
<|DATE|>'''
a = input("Enter your name")
b = input("Enter the date")
str = str.replace("<|NAME|>","Rishi")
str = str.replace("<|DATE|>","29/6/2020")
print(str)