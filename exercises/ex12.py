def word_histogram(sentence): # Create a function with a string parameter
    num_of_words = {}  #Declare an empty dic
    words = sentence.split()    #Create a list of the words in the sentence

    for word in words:  #for each word in the list
        if word in num_of_words:    #Check if word is inside the dict
            num_of_words[word] += 1 #if it is, add one to the value of that key
        else:   #if the word is not in the dict
            num_of_words[word] = 1  #add a new key with that word, with value 1
    print(num_of_words)     #print dict once loop is over

word_histogram("three three three two two one")     #call function with a string.