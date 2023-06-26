
def array_to_string():
    array = [1, 2, 3]
    num_str = ''
    for num in array:
        num_str += str(num)
    return num_str

result = array_to_string()
print(result)