""" NAME: Srishu Chintakindi
ID: 20CE012
GitHub repositary link: https://github.com/srishu272/Python_Programming
Practical:6
You are given n words. Some words may repeat. For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. See the sample 
input/output for clarification.

Sample Input
4
bcdef
abcdefg
bcde
bcdef

Sample Output
3
2 1 1

Explanation: There are 3 distinct words. Here, "bcdef" appears twice in the input
at the first and last positions. The other words appear once each. The order of the
first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the
output."""

N = int(input())
str_list = []
cnt_dict = {}

for i in range(N):
    s = input()
    str_list.append(s)

    if s in cnt_dict:
        cnt_dict[s] += 1
    else:
        cnt_dict[s] = 1
    
print(len(cnt_dict))
print(' '.join([str(cnt_dict[s]) for s in cnt_dict]))