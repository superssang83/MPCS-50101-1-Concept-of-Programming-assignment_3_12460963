def centered_average_with_iteration(numbers): 
    if len(numbers) < 3:
        raise ValueError("List must contain at least three numbers.")
    
    total = 0
    min_value = min(numbers)
    max_value = max(numbers)
    
    for num in numbers:
        total += num

    centered_total = total - min_value - max_value
    average = centered_total / (len(numbers) - 2)
    
    return average 

def centered_average(numbers):
    if len(numbers) < 3:
        raise ValueError("List must contain at least three numbers.")
    
    sorted_numbers = sorted(numbers)
    trimmed_numbers = sorted_numbers[1:-1]

    if trimmed_numbers:
        average = sum(trimmed_numbers) / len(trimmed_numbers)
    else:
        average = 0
    
    return average 

numbers = [1, 4, 5, 6, 100]

print(f"1. Iteration: {centered_average_with_iteration(numbers)}")
print()
print(f"2. Non-iteration: {centered_average(numbers)}")
print()
