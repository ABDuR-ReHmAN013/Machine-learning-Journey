
def largest_number(numbers):
    if not numbers:  
        return None
    max_num = numbers[0]       # Assume the first number is the largest
    for num in numbers:        # Loop through the list
        if num > max_num:      # If we find a bigger number
            max_num = num      # Update max_num
    return max_num             # Return the largest number

# Example usage
nums = [4, 7, 2, 9, 1]
print("List:", nums)
print("Largest number:", largest_number(nums))
