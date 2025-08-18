def deco(func):
    def wrapper(*args, **kwargs):
        print('Before function call....')
        out = func(*args, **kwargs)
        print('After function call....')
        return out
    return wrapper


@deco
def hello():
    return 'Hello decorator ....'

print(hello())



def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper



# old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
# new_list = old_list
 
# new_list[2][2] = 9
 
# print('Old List:', old_list)
# # [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]

# print('ID of Old List:', id(old_list))
 
# print('New List:', new_list)
# #  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print('ID of New List:', id(new_list))


# # Old List: [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
# # ID of Old List: 242342343535

# import pandas as pd

# # df = pd.read_csv('txt.csv')

# # name = df[df['student'] == 'ashok']


# # Name	Subject
# # Ashok	Maths
# # Danish	Maths,Phy
# # Xyz	Bio
# # Abc	Pys,Maths

# find all stundent name   subject with math

# how to drop null value in pandas 
# # mro in python 
# desing pattern using class

# # name = 

# mysq engines 
# write indexin in sql 
# compound index 

 
