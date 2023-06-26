from exercises import ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8,ex9, ex10, ex11



def main():
    # ex1.hello_world("5")
    # ex2.array_to_string()
    # ex3.add_numbers()
    #  EX4:
     sentence = input('Enter sentence:')
     num_words =ex4.count_words(sentence)
     print(num_words)

     # EX5:
     sentence1 = "Test.  This is a test.  Testing."
     sentence2 = ex5.replace_period(sentence1, "!")
     print(sentence2)

    #EX6
     ex6.slice_it(["this", "is", "another", "test"])


    #EX7
     array = [2.00, 4.00, 4.00]
     tax = "10%"
     result = ex7.calc_total(array, tax)
     print(result)


    #EX8
print(ex8.f_to_c(22))
print(ex8.c_to_f(-6))


#EX 9

print(ex9.num_vowels)

#EX 11
ex11.diagonal_printer("this is a test")

#Ex 10

while True:
 result =  ex10.calculator()

#building method. Execute main if the function at the bottom is main.
if __name__ == '__main__':
    main()

