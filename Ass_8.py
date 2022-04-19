""" NAME: Srishu Chintakindi
ID: 20CE012
GitHub repositary link: https://github.com/srishu272/Python_Programming
Practical:
Program to demonstrate the Overriding of the Base Class method in the Derived Class."""

class Parent():

   def volume(self,l,b,h):
        self.vol = l*b*h
        print(self.vol)
        print("Inside Parent")

class Child(Parent):

    def volume(self,l,b,h):
         if(l==b and l==h):
              self.vol = l**3
              print(self.vol)
              print("Inside Child")
         else:
             super().volume(l,b,h)

l=int(input("Enter l:"))
b=int(input("Enter b:"))
h=int(input("Enter h:"))

obj = Child()
obj.volume(l,b,h)