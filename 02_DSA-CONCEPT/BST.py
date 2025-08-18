class BSTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if self.data == data:
            return   #Node already exist
        # left
        if self.data > data:
            if self.left:
                # insert into left subtree
                self.left.addChild(data)
            else:
                self.left = BSTree(data)
        # right        
        else:
            if self.right:
                # insert into right subtree
                self.right.addChild(data)  
            else:
                self.right = BSTree(data)      
    
    def inOrder_Traversal(self): # it is a sorting
        elements = []
        # visit left subtree
        if self.left:
            elements += self.left.inOrder_Traversal()
        elements.append(self.data)

        # visit right subtree  
        if self.right:
            elements += self.right.inOrder_Traversal()

        return elements    




def buildTree(elements):
    print("Given element", elements)
    root = BSTree(elements[0])
    for i in range(1, len(elements)):
        root.addChild(elements[i])
    return root   

if __name__ == '__main__':
    # numbers = [17,4,1,20,9,23,18,34]
    numbers = ["India","Pakistan","Australia","Usa","China","Uae","Afganistan"]

    root = buildTree(numbers)
    # print(root) 
    print(root.inOrder_Traversal())
        