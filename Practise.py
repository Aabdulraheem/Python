# example 1 : String input and output
# EXpected input = "john"
# expected output = "Hello,john!"
"""
a = int(input("givve a number: "))
b = int(input("give b value: "))

print(a,b,a,b, sep = ",", end = ".")

"""
# Examp;e 1:   string input and output 
# Sreing input an output 

# Expecred input : "john"
# expected output : "Hello,john!""

"""
name = input("Enter a name:")
print("Hello",name,sep =",",end="!")


"""
# Example 2 :  integer input and output

# Expected input 5
# Expected output "You entered :5"
"""
num = int(input("ENter a num:"))

print("You Entered:",num,sep="")

"""

# exxample 3: Float inpuit and output 
# Expected input : 3.14
# Expected output : "Value of Pi: 3.14"

"""pi = float(input("Enter pi value:"))

print("Value of Pi:",pi,sep = "")
"""


# Exmple 4 : Taking multiple inputs in a single line
# expected input 10 20 30 
# Expected ouptput : "sim of inputs : 60"

"""
a = input("Enter three numbers seperated by space: ")

x ,y, z = a.split(" ")

sum = int(x) + int(y) + int(z)

print(sum)

"""

# Ex 5 :specifiing seperator in output 
# EXp inp : "john",25
# Exp out : "Name:John,Age:25"

"""
inp = input("enter name and age: ")
name,age = inp.split(",")

print("Name:",name, ",Age:",age,sep="")

"""

# EX- 6 End parameter in output 
# Ex inp : 5
# exp out : "Countdown: 5 4 3  2 1 Blast off!"
"""
num = int(input("Enter n: "))

print("countdown : 5 4 3 2 1 ",  end = "Blast off!")

"""

# Example 7 - Arihtmetic Operators 
# Expected inout - 10,5
# Expected output- "Addition: 15,sub - 5, mul=50.div-2.0
"""
x,y = input("enter a and b values:").split(",")
a = int(x)
b = int(y)

print("Addition:",a+b,"Subtraction:",a-b,"Multiplication:",a*b, sep = ",")
"""
"""
Multiple = input("ENter 3 numbers:")

x,y,z = Multiple.split(" ")

sum = int(x) + int(y) + int(z)

print("Sum of the numbers:",sum)

"""

# Exampole 8: comparision Operators
# Expected input : 10,5 
# xpected output : "10 > 5: True,10<5 : false, 10==5: False,10!=5 :True"
"""

a = 10 
b = 5

print("10>5:",a>b,"10<5:",a<5, "10==5:",a == b, "10!=5:",a == b)
"""

# 9 LOgical OPerators 
# expected input : True , False
# expected ouptput : "Truw and Flasw, True or False: True,not True : False "
"""
T = True
F= False

print("True and Flase:",T and F, ",True or False:",T or F,",Not True :", not T)

"""

# EX : 10 , Raking Yes/No input and Handling case Sensitivity 
# Expected input : Yes(or yes,YES,yES,etc.)
# expected output : "You entered : Yes"
"""
y = "Yes"
n= "no"

print("You entered : ",y)

"""

# E- 11 Formation output using f-strings
# ex -in : "ALice",25
# Ex-out : "NAme : ALice , age : 25 Years"


a,b = input("Enter Name and Age: ").split(",")
print(f"Name :{a}, Age:{b} years")
















