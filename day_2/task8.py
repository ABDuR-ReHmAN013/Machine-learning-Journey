numbers=[1,2,3,4,5,6,7,8,9,10]
def square(numbers):
    squares=[]
    for num in numbers:
        square=num**2
        squares.append(square)
    return squares

print(square(numbers))