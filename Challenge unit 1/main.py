#implement a recursive functionto calculate the factorial of a given number.
"""
  1!= 1 x1
21-2x12x1
31-3-21--->3×2×1
.
.
101-10x91--->10x9x8x7x6x5x4×3×2×1

formula nx(n-1)!
"""



def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)

number= int(input("Enter a value:"))
res=fact_rec(number)

print("The factorial of {} is{}.".format(number, res))