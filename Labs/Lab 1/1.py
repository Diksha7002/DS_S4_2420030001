"""
# here end=" " helps to print the next statement in the same line
print("Hi i'm DIKSHA YADAV",end=" ")

#here sep="-" helps to print the next statement with a separator
print("Hi","how are you?",sep="-")

#here we can use the input function to take input from the user
str=input("Diksha Yadav")
print(str)

#here type function to know the data type of the variable
a=5
b=2.5
c="Hello"
d=True
print(type(a),type(b),type(c),type(d))

#this is an example of type casting
#as we use int the data types of all the variables will be converted into integer
x=int(1)
y=int(2.8)
z=int("3")
print(x,y,z)

#here as we use float the elements will be converted into float
x=float(1)
y=float(2.8)
z=float("3")
print(x,y,z)

#here we the same with string
x=str("s4")
y=str(2)
z=str(3.0)
print(x,y,z)

a="Hello, World!"

#use triple quotes to print the string in multiple lines

b=I am a student at KL University, in Hyderabad.
#I'm currently in my 3rd year of B.Tech.
#print(a,b,end=" ")


#this is called string slicing in python
a="My name is Diksha Yadav."
print(a[11:])
print(a[:10])
print(a[11:17])
print(a[-17:-11])

#this is an example of string methods in python
a="KONERU LAKSHMAIAH EDUCATIONAL foundation"
b="KLh"
print(a.lower())
print(b.upper())
print(a.find("D"))
print(a.capitalize())
print(b.capitalize())
print(a.swapcase())
print(b.swapcase())
print(a.title())
print(len(a))
print(len(b))

#for concatenation of strings we can use + operator
a="Hello"
b="World"
c=a+b
c=a+" "+b
print(c)

#Stirng format() method
a="My name is {fname}.I am {age} years old.".format(fname="Priya",age=25)
b="My name is {0}.I am {1} years old.".format("Priya",25)
c="My name is {}.I am {} years old.".format("Priya",25)
print(a)
print(b)
print(c)
"""