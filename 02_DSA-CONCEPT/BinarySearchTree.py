class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data 
            return
        if self.key == data:
            return
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)                
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self, data):
        if self.key == data:
            print("Node is Found :)")
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not found in  left tree :{")
        else :
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not found in right tree :{")    

    def preOrder(self):
        print(self.key, end = "->") 
        if self.lchild:
            self.lchild.preOrder()  
        if self.rchild:
            self.rchild.preOrder() 

    def InOrder(self):
        if self.lchild:
            self.lchild.InOrder()  
        print(self.key, end = "->") 
        if self.rchild:
            self.rchild.InOrder()  

    def postOrder(self):
        if self.lchild:
            self.lchild.postOrder()  
        if self.rchild:
            self.rchild.postOrder()        
        print(self.key, end = "->") 

    # def maxHeight(self):
    #     if self.lchild:
    #        l =  self.lchild.maxHeight()
    #     if self.rchild:   
    #        r =  self.rchild.maxHeight()
    #        return 1+max(l,r)
    #     else:
    #         return -1


    def delete(self, data):
        if self.key is None:
            print("Tree is Empty :{")
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Node is not found in left tree :{")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Node is not found in right tree :{")    
        else:
            if self.lchild is None:
                tmp = self.rchild
                self = None
                return tmp
            if self.rchild is None:
                tmp = self.lchild
                self = None
                return tmp  
            
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)  
        return self   


    def minNode(self):
        current = self
        while current.lchild: #run till lchild become none
            current = current.lchild
        print("Node with smallest key is:", current.key)

    def maxNode(self):
        current = self
        while current.rchild: #run till rchild become none
            current = current.rchild 
        print("Node with maximum key is:", current.key)         

root = BST(10)
lst = [6, 3, 1, 6, 98, 3, 7]
for i in  lst:
    root.insert(i)

print('---PreOrder---')
root.preOrder()
print()
# print('---InOrder---')
# root.InOrder()
# print()
# print('---PostOrder---')
# root.postOrder()

root.delete(6)
print('---PreOrder after deleting ---')
root.preOrder()

# print()
# root.minNode()
# root.maxNode()
# root.maxHeight()



