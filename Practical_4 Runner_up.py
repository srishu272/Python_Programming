#NAME: Srishu Chintakindi
#ID: 20CE012
#GitHub repositary link: https://github.com/srishu272/Python_Programming
#Practical:4
#Find runner-up from given list
#Sample Input
#5
#2 3 6 6 5
#Sample Output
#5
#Explanation: Given list is [2,3,6,6,5]. The maximum score is 6, second
#maximum is 5. Hence, we print 5 as the runner-up score.


n=int(input()) #taking input of the number of elements in the list
scores=list(map(int,input().split(" "))) #taking input of the list
scores = sorted(scores) #sorting the list

score_set = set(scores) #converting list into set
Max_score = max(score_set) #finding the maximum of the set
score_set.remove(Max_score) # Removing the maximum of the set
Max_score = max(score_set) #Again finding the maximum which will now give me the secong maximum number of that set
print(Max_score)


