def to_alternating_case(string):
    result = ""
    for letter in string:
        #Check to see if the letter is lower
        if letter.islower():
            #Converts lowercase to uppercase
            result += letter.upper()
        else:
            #Converts uppercase to lowercase
            result += letter.lower()
    return result


#Another example
def alternate_casing(stringg):
    return stringg.swapcase()