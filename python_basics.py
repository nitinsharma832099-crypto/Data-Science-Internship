# #: Learn variables, data types, operators, loops, functions and write simple Python programs.
# #variable
name="xyz"
age=18
height=5.6 

print(name)
print(age)
print(height)

# #Datatypes
print(type(name))
print(type(age))
print(type(height))

#operators
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication",a*b)

#loops
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

for k in range(5, 0, -1):
    for l in range(k):
        print("*", end="")
    print()
 


# #if-else
age=int(input("Enter your age:"))
if age>=18:
  print("Eligible to vote")
else:
  print("Not eligible to vote")  

#function
def cube(num):
    return num * num*num

print("cube of 6:", cube(6))