#create a function that accepts strings
def slice_it(array):    #creating a function with a list parameter
   new_string = ''      #Declaring a variable as an empty string
   for word in array:
      new_string += word[0:2]    #taking first 2 letter of each word and adding them to the empty string
   return new_string      #Returning the new word made out of the first 2 letter of each word


print(slice_it(["this", "is", "another", "test"]))

# or

#def slice_it(strings)
   #new_string = ''

   #for word is strings:
      #new_sring += word[0] + word[1]
   # return new_string