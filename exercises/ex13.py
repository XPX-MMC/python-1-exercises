def frame_it(word_list):    #Create a function that takes in a list
    longest_word = 0    #initiate a variable to determine the longest word
    stars = ''  #empty string to save the stars later

    for word in word_list:  #for each word on the list
        if len(word) > longest_word:    #Check if the length of the current word is longer than the longest word
            longest_word = len(word)    #if it is assign that value to the variable
        stars = '*' * longest_word + '****'     #generating starts base on the longest word of the list

    print(stars)       #print first row of stars
    for word in word_list:  #for each word on the list
        print(f"* {word} {' ' * (longest_word - len(word))+ '*'}")  #print * , them a space based on the length of each word *
    print(stars)    #print last row of stars

wordlist =["Hello","World","in","a","frame"]    #list of words
frame_it(wordlist)  #calling function with the last of words.