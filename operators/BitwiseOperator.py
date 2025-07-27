# bitwise Operators in python 

# Bitwise AND (&) : 

a = 2
b = 3

c = a & b
print("the biteise operaot and (&):",c)  # output: 2

# Bitwise operator OR (|) : 

d = a | b
print("the bitwise OR (|):" , d)   # output: 3

# Bitwise operator XOR (^):

e = a ^ b
print("the bitwise xor (^):", e)   # output: 1

# Bitwise operator NOT (~):
f = ~ a
print("bitwise NOT (~) :", f)   # output: -3


# Bitwise operator rigth shift (>>)

print(2>>1)    # output: 1

# Bitwise operator left shift (<<)

print(2<<1)     # output: 4


# Bitwise left shift <<

result_left_shift = 2 << 2
print("Bitwise left shift:", result_left_shift)  # output: 8

# Bitwise right shift >>

result_right_shift = 32 >> 2
print("Bitwise right shift:", result_right_shift)   # output: 8
