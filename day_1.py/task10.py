def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Even numbers:", get_even_numbers(numbers))
