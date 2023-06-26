def calc_total(array, tax): #Create function with 2 parameters : a list of prices and a string tax
    sum = 0      #Declare a variable for the sum of all elements on the list
    tax_num= int(tax.rstrip("%"))   #turn tax string into an int and remove  '%'
    price = 0.0     #Declare variable to calculate total price including price.

    for nums in array:  #start iterations
        sum += nums     #Adding all the numbers inside of the list together.
    price = "${:,.2f}".format(sum*(tax_num/100)+sum)    #Calculate the total price with taxes and format to add '$' and trim flaot number to 2 decimals
    return price    #Return total price



# array = [2.00, 4.00, 4.00]
# tax = "10%"
# result = calc_total(array, tax)
# print(result)




