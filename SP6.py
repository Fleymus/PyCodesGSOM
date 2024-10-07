def find_two_smallest(numbers):
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements.")
    
    smallest = float('inf')
    second_smallest = float('inf')
    
    for number in numbers:
        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif number < second_smallest and number != smallest:
            second_smallest = number
    
    if second_smallest == float('inf'):
        raise ValueError("The list must contain at least two distinct elements.")
    
    return smallest, second_smallest