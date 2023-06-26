def vowel_counter(string):
    vowel_count = 0
    for eachChar in string:
        if eachChar in 'aeiouAEIOU':
            vowel_count+= 1
    return f"Number of vowels: {vowel_count}"
sentence= "This is a test"
num_vowels = vowel_counter(sentence)
print(num_vowels)


# def vowel_counter(sentence):
        #vowels = ['a','e'.'i','o','u','A','E','I','O','U']
        #counter = 0

        #for letter in sentence:
            #for vowel in vowels:
                #counter += 1
                #break
        #return f"Number of vowels:{counter}"

#sentence = "This is a test"
#num_vowle = vowel_counter(sentence)
#print(num_vowels)
