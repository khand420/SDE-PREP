# Check if two strings are permutations of each other


def isPermutation(string1, string2) :
    
    #Your code goes here
    return sorted(string1) == sorted(string2)


string1= "sinrtg" 
string2 = "string"

print(isPermutation(string1, string2))

