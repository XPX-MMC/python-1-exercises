def ex1(times):
    num_times = None

    if times.isdigit():
        num_times = int(times)

    if num_times is not None:
        print("\n".join(["hello world here i come!"] * num_times))

ex1("3")


# def ex2(array):
def array_to_string(array):
    result = ''
    for element in array:
        result += str(element) + ', '
    result = result.rstrip('')
    return result

array = [1, 2, 3]
result = ', '.join(str(element) for element in array)
print (result)

    

def ex3():
    print("ex 3")


def ex4():
    print("ex 4")


def ex5():
    print("ex 5")


def ex6():
    print("ex 6")


def ex7():
    print("ex 7")


def ex8():
    print("ex 8")


def ex9():
    print("ex 9")


def ex10():
    print("ex 10")

#
# Place your functions here...
#
