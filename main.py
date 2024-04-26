                                #DAY1

#1
print("A 'single quote' inside a double quote")
print('A "double quote" inside a single quote')
print("Alternatively you can just \"escape\" the quote")

#2
print("Hello"+" "+"Anamika")

#3
print("Hello" +" "+ input("what's your name? "))

#4
n1=int(input("Enter first no. "))
n2=int(input("Enter second no. "))
print(n1+n2)

#5
name=input("name pls? ")
print(name)

name="Anabelle"
print(name)

name = input("Enter your name: ")
length = len(name)
print(length)

#6 swapping two variables
a = input()
b = input()

temp=a
a=b
b=temp

print("a: " + a)
print("b: " + b)

#or

# There are two variables, a and b
a = input()
b = input()
# Create a third variable to help switch the values
c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

#7 DAY1 FINAL PROJECT
print("Welcome to the Band Name Generator.")
street = input("What's name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)
                                # DAY1