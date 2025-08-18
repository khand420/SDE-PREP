
def outer(func):

    def inner():
        print("hello mobifly")
        func()
        print("By mobifly")
        return "hi"
    return inner

@outer
def myFunc():
    print("Bye Mobifly")

# a = outer(myFunc)
# p = a()

myFunc()

# print(p)