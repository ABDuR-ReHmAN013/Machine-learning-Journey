n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
n3=int(input("Enter third number"))
def find_maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c        