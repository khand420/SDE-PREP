# Question : write a program to find number of occurrence of each vowel present in a given string

s = 'Hello, world!'
vowel = 'aeiou'
counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for i in s:
    if i.lower() in vowel:
        counts[i.lower()] += 1
        
print(counts)


# Question : write a program to find primefactors of a number
n = 50
i = 2
factor = []
while i<=n:
    if n%i == 0:
        factor.append(i)
        n = n//i
    else:
        i+=1
print(factor)            


# Question : Write a program that prints the numbers from 1 to 100. But for multiple of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizBuzz"
# Question : wrtite a program to reverse the words of a string at its own position & the first and last character of every word should be capital?

# Example
# =========

# Input 
# ======
# string = 'How are you'

# Output
# ========
# output = 'WoH ErA UoY'
string = 'How are you'
output = ' '.join([word[::-1] for word in string.split()]).swapcase().title()
# print(output)


string = 'How are you'
output = ''
for word in string.split():
    reversed_word = word[::-1]
    for i in range(len(reversed_word)):
        if i % 2 == 0:
            output += reversed_word[i].upper()
        else:
            output += reversed_word[i].lower()
    output += ' '
print(output[:-1])


string = 'How are you'
words = string.split()
output = words[0][0].upper() + words[0][1:][::-1]
for word in words[1:]:
    output += ' ' + word[::-1]
# print(output)






# Output 
# 	a - b = [2,5,5,6,8,4,4,0,9,4]
a = [4, 8, 9, 6, 7, 5, 6, 7, 8, 1]
b = [2, 3, 3, 9, 9, 1, 2, 6, 8, 7]

result = [0] * len(a) # initialize result list with zeros

for i in range(len(a)):
    result[i] = a[i] - b[i]

print(result)



# Question : write a script to store Subject and Marks into a dictionary by taking inputs from users and display the records as a dictionary?
# Example:

# 	Enter no of records :  2
# 	Enter Subject : Maths
# 	Enter Marks : 80
# 	Enter Subject : English
# 	Enter Marks : 70
	
# 	results : {'Maths':80,'English':70}
# num_records = int(input("Enter no of records: "))
# result = {}

# for i in range(num_records):
#     subject = input("Enter Subject: ")
#     marks = int(input("Enter Marks: "))
#     result[subject] = marks

# print("Results:", result)





    





