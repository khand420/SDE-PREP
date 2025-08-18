from functools import reduce

# Example: Calculate the product of a list of numbers
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# lst = [1,2,3,4,5]
# # outp : [1,2,3,8,10]

# # outp : [1,2,3,8,10]
def mapdata(i):
    if i > 3:
        return i * 2
    else:
        return i    
    # return i
lst = [1,2,3,4,5]

result = list(map(lambda x: x*2 if x > 3 else x, lst))
mul = list(map(mapdata ,lst))




# mapping = {4: 8, 5: 10}
# # Use map with a lambda function to apply the mapping
# result = list(map(lambda x: mapping.get(x, x), lst))


# print(mul)
print(result)




# s = ['aass','dccfd','rdff','tygg','gftty','tyuuy','fthhb']

# # 'tygg'
# # gftty'
# # 'tyuuy',
# # fthhb
# ind = s.index('rdff')
# for i in range(ind+1, len(s)):
#     print(s[i]) 



# def deco(func):
#     def wrapper(*args,**kwargs):
#         print('Before func call')
#         out = func(*args,**kwargs)
#         print('Afer func call')
#         return out
#     return wrapper

# @deco
# def hello():
#     print('Hello')

# hello()    


# t  = [('a', 47),('b', 33),('c',78),('d', 58),('e', 66)]


# s = sorted(t, key= lambda x:x[1])

# print(s)


