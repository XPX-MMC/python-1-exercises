
def ex1():
    hello_world("3")


def ex2():
    array = [1, 2, 3]
    result = array_to_string(array)
    print(result)


def ex3():
    array = [1.0, 1.1, "1"]
    result = add_numbers(array)
    print(result)


def ex4():
    sentence = input("Enter sentence: ")
    num_words = count_words(sentence)
    print(num_words)


def ex5():
    sentence = "Test.  This is a test.  Testing."
    sentence2 = replace_period(sentence, "!")
    print(sentence2)


def ex6():
    array = ["this", "is", "another", "test"]
    r = slice_it(array)
    print(r)


def ex7():
    array = [2.00, 4.00, 4.00]
    tax = "10%"
    result = calc_total(array, tax)
    print(result)


def ex8():
    print(f_to_c(22))
    print(c_to_f(-6))


def ex9():
    sentence = "This is a test"
    num_vowels = vowel_counter(sentence)
    print(num_vowels)


def ex10():
    while True:
        result = calculator()
        print(result)


def ex11():
    diagonal_printer("This is a test")


def ex12():
    word_histogram("three three three two two one")


def ex13():
    wordlist = ["Hello", "World", "in", "a", "frame"]
    frame_it(wordlist)


def frame_it(array):
    len_longest_word = 0
    for word in array:
        if len(word) > len_longest_word:
            len_longest_word = len(word)
    print(create_separator(len_longest_word))
    for word in array:
        print(create_text_line(word, len_longest_word))
    print(create_separator(len_longest_word))


def ex14():
    print("TODO: Ex. 14...")


def ex15():
    print("TODO: Ex. 15...")


#
# Place your functions here...
#

def hello_world(num):
    num = int(num)
    for x in range(num):
        print("Hello World from Python!")


def array_to_string(array):
    retval = ""
    for i in array:
        retval += (str(i) + " ")
    return retval


def add_numbers(array):
    retval = 0.0
    for i in array:
        retval += float(i)
    return retval


def count_words(sentence):
    retval = 0
    word_array = sentence.split(" ")
    for word in word_array:
        if len(word) > 0:
            retval += 1
    return "Number of words: " + str(retval)


def replace_period(sentence, puncuation):
    retval = ""
    for letter in sentence:
        if letter == ".":
            retval += puncuation
        else:
            retval += letter
    return retval


def slice_it(array):
    retval = ""
    for w in array:
        retval += w[0:2]
    return retval


def calc_total(array, tax):
    retval = 0.0

    # Calculate total.
    for i in array:
        retval += i

    # Add taxes.
    tax_rate = float(tax[:-1])/100
    taxes = retval * tax_rate
    retval += taxes

    # Format output.
    retval = "${:,.2f}".format(retval)
    return retval;


def f_to_c(value):
    celsius = round((value-32) * (5/9))
    return f'{str(value)} degrees Fahrenheit is {celsius} degrees Celsius.'


def c_to_f(value):
    far = round(value * 9/5 + 32)
    return f'{str(value)} degrees Celsius is {far} degrees Fahrenheit.'


def vowel_counter(sentence):
    retval = 0
    vowels = "aeiou"
    for letter in sentence:
        if letter in vowels:
            retval += 1
    return f"Number of vowels: {retval}"


def calculator():
    retval = 0
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    operation = input("Enter operation (+, *, /, -): ")
    if operation == "+":
        retval = num1 + num2
    elif operation == "*":
        retval = num1 * num2
    elif operation == "/":
        retval = num1 / num2
    elif operation == "-":
        retval = num1 - num2
    return retval


def diagonal_printer(input_string):
    my_word_list = input_string.split(' ')
    for word in my_word_list:
        for idx in range(len(word)):
            padding = ''
            for _ in range(idx):
                padding += ' '
            print(f'{padding}{word[idx]}')


def word_histogram(sentence):
    word_dict = {}
    words = sentence.split(" ")
    for word in words:
        count = word_dict.get(word)
        if count is None:
            word_dict[word] = 1
        else:
            count += 1
            word_dict[word] = count
    print(word_dict)


def create_separator(length):
    retval = ''
    for _ in range(length + 4):
        retval += '*'
    return retval


def create_text_line(word, len_longest_word):
    retval = ''
    end_string = ''
    num_spaces_to_add = (len_longest_word - len(word)) + 1
    for _ in range(num_spaces_to_add):
        end_string += ' '
    end_string += '*'
    retval = f'* {word}{end_string}'
    return retval
