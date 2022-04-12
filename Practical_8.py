''' 
NAME: Srishu Chintakindi
ID: 20CE012
GitHub repositary link: https://github.com/srishu272/Python_Programming
Practical:8

Write a Program in Python to implement a Stack Data Structure using Class and Objects, 
with push, pop, and traversal method.
'''

class stack:
    element = []
    def _init_(self):
        self.element=[]
        top=None
        #We use a list to form a stack which have predefined functions like append for push and pop

    #push operation
    def push(self,key):
        self.element.append(key)
        print('Key Pushed')


    #pop function
    def pop(self):
        return self.element.pop()


    def traversal(self):
        for i in (self.element):
            print(i)


Stack_=stack()

Stack_.push(10)
Stack_.push(20)
Stack_.push(30)
print("Displaying the elements")
Stack_.traversal()
Stack_.pop()
Stack_.pop()
print("Displaying the elements after 2 pop()")
Stack_.traversal()