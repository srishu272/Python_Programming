""" NAME: Srishu Chintakindi
ID: 20CE012
GitHub repositary link: https://github.com/srishu272/Python_Programming
Practical:7
Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters 
and same frequency of each character. If there are odd number of characters in the string, we ignore the middle
character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same
characters with same frequency. Also, abccab, rator and xyzxy are a few examples of lapindromes. Note that abbaab 
is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match. Your task is 
simple. Given a string, you need to tell if it is a lapindrome.
Input: 6
gaga 
abcde
rotor
xyzxy
abbaab
ababc

Output:
Yes 
No 
Yes 
Yes 
No 
No """


N = int(input())
str_list =[]
for i in range(N):
    s = input()
    str_list.append(s)

for i in range(N):
    s = str_list[i]
    length = len(s)
    mid = int(length/2)
    if(length%2==0):
        s1 = s[:mid]
        s2 = s[mid:]
    else:
         s1 = s[:mid]
         s2 = s[mid+1:]
    list_1 = list(s1)
    list_2 = list(s2)
    list_1.sort()
    list_2.sort()

    if(list_1 == list_2):
        print("Yes")
    else:
         print("No")