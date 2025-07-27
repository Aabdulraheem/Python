# Solving Quadratic Equations
# Sample input = a = 1, b= -3 , c = 2
# sample output = Roots:(2.0,1.0)

# Topics covered : input and output , variables , Arithemetic operators. 
#  ax ^ 2 + bx + c = 0 


                                # -b +- root(b^2 -4ac) / 2a

a = int(input("a:"))
b= int(input("B:"))
c= int(input("c:"))

d = (b**2) - 4*a*c

root1 = (-b +(d**(0.5))) / (2*a)
root2 = (-b - (d**(0.5) ))/(2*a)

print(f"roots:({root1},{root2})")