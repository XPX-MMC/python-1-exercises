def add_numbers(array):
    x = 0
    for num in array:
         x += float(num)
    return x
result = add_numbers([1.0, 1.1, "1"])
print(result)


