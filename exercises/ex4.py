def count_words(sentence):  #create function that takes a string variable
    num_words = {} # declaring empty dictionary
    words = sentence.split()  #creating a list with the words in my sentence, and splitting the words by the spaces
    total = 0   #declaring a counter variable and intializing it to 0

    for word in words: #looping through my list of words, each word is declared as "word"
        if word in num_words:   #adding a condition if the word is already in the dict
            num_words[word] += 1   #add 1 to the current value
            total += 1  #adding to the total words variable
        else:   #if the words is NOT in the dictionary
            num_words[word] =1  #adding the word and giving it a value of 1
            total += 1  #adding 1 to my total words counter
    return total    #returning my total.

#to test the program
# sentence = input("Enter sentences: ")   #input from the user
# num_words = count_words(sentence)   #creating num_words variable and assigning the return of my function
# print(num_words)    #priting the result


# or
# def count_words(sentence):

# word_count = 1
# in_space = False

# loop thru all characters of string
# update counter after finding a ' (space)
# for char in sentence:
#     if char == '':
#         word_count += 1
#    word_count +=

# return count(int)
#  return word_count

# this is a test


