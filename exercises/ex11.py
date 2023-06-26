def diagonal_printer(str):  #Create a function that takes a string parameter
    list_str = str.split()  #split the words and save them in a list

    for word in list_str:   #loop through each word of the list
        for i in range(len(word)):  #loop through each letter of each word
            #printing the space, multiplying by i.
            print(' ' * i, word[i]) #multiply space by the pasition of the letter in the word and then print letter.

diagonal_printer("this is a test")  #calling the function