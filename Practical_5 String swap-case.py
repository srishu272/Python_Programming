#NAME: Srishu Chintakindi
#ID: 20CE012
#GitHub repositary link: https://github.com/srishu272/Python_Programming
#Practical:5
#You are given a string and your task is to swap cases. In other words, convert
#all lowercase letters to uppercase letters and vice versa.
#Sample Input: HackerRank.com presents "Pythonist 2".
#Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".

string = input() #taking input of the string
swap = []

for i in range(len(string)): # taking a loop from 0 to length of string

     if(string[i].islower()): #checking if the character in string are lowercase
         swap.append(string[i].upper()) #appending them into swap after converting to uppercase
         
     elif(string[i].isupper()): #checking if the character in string are uppercase
         swap.append(string[i].lower()) #appending them into swap after converting to lowercase
         
     else: #otherwise the character is just a symbol or white space
         swap.append(string[i]) #appending that character directly to swap
string1 = ""
print(string1.join(swap)) #printing the new string by joining swap
