def sum_first_last(numbers):
    if len(numbers) == 1:
        first_val = numbers[0]
        return first_val + first_val
    else:
        first_val, *middle_vals, last_val = numbers
        return first_val + last_val

output1 = sum_first_last((1, 2, 3, 4, 5))
print(output1)
output2 = sum_first_last((10, 20))
print(output2)
output3 = sum_first_last((7,))
print(output3)