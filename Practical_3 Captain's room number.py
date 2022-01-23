#NAME: Srishu Chintakindi
#ID: 20CE012
#GitHub repositary link: https://github.com/srishu272/Python_Programming
#Practical:3
#Find Captain Room Number
#Sample Input
#5
#1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
#Sample Output
#8
#Explanation: The list of room numbers contains 31 elements. Since K is 5, there
#must be 6 groups of families. In the given list, all of the numbers repeat 5 times
#except for room number 8.
#Hence, 8 is the Captain's room number.


K=int(input()) #taking input of number of family groups
room_nos=list(map(int,input().split(" "))) #taking input of the 31 elements
room_nos = sorted(room_nos) #sorting the list

for i in range(len(room_nos)): #loop of i from 0 to the number of elements in the list
    if(i != len(room_nos)-1):
        if((room_nos[i] != room_nos[i-1]) and (room_nos[i] != room_nos[i+1])): #checking for the element that is not repeated
            print(room_nos[i])
            break;
    else:
        print(room_nos[i])