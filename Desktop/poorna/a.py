def find_greatest_number(arr):
    if not arr:
        return None  # Return None for an empty array

    greatest_number = arr[0]

    for number in arr:
        if number > greatest_number:
            greatest_number = number

    return greatest_number

# Example usage:
numbers = [5, 8, 2, 10, 3, 15, 7]
result = find_greatest_number(numbers)

print(f"The greatest number in the array is: {result}")
