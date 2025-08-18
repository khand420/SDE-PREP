class stack:
    def __init__(self):
        self.list = []

    def push(self, data):
        return self.list.append(data) 

    def pop(self):
        if not self.list:
            print("Stack is empty")
        else:
           return self.list.pop()          

    def isEmpty(self):
        if not self.list:
            print("Stack is empty")
        else:
            print("Stack is not empty", self.list)    


ob = stack()
ob.push(1)
ob.push(2)
ob.push(3)

ob.pop()

ob.isEmpty()

