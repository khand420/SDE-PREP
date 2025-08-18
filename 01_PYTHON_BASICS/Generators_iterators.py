#1. iterator
iter_list = iter(['Geeks', 'For', 'Geeks'])

print(type(iter_list))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))




#2. Generator
def sq_numbers(n):
	for i in range(1, n+1):
		yield i*i


a = sq_numbers(3)


print("The square of numbers 1,2,3 are : ")
print(next(a))
print(next(a))
print(next(a))


# iter() keyword is used to create an iterator containing an iterable object.
# next() keyword is used to call the next element in the iterable object.




# Iterator	Generator
# Class is used to implement an iterator

# Function is used to implement a generator.

# Local Variables aren’t used here.                                         

# All the local variables before the yield function are stored. 

# Iterators are used mostly to iterate or convert other objects to an iterator using iter() function.                                                               	Generators are mostly used in loops to generate an iterator by returning all the values in the loop without affecting the iteration of the loop
# Iterator uses iter() and next() functions 	Generator uses yield keyword
# Every iterator is not a generator	Every generator is an iterator