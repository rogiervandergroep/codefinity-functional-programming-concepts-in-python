def unpack_first_last(list):
    first_val, sec_val, *middle_vals, one_last_val, last_val = list
    result = (first_val, sec_val,  one_last_val, last_val )
    return result

res1 = unpack_first_last([1, 2, 3, 4, 5, 6])
print(res1)
res2 = unpack_first_last(['a', 'b', 'c', 'd'])
print(res2)
res3 = unpack_first_last([10, 20, 30, 40, 50])
print(res3)