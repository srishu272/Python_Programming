#Write a python script to check whether a given key already exists in a dictionary.
d = {10:1,20:2,3:13,}
def has_key(x):
  if x in d:
      print('THE MENTIONED KEY IS PRESENT IN THE ABOVE DICTIONARY')
  else:
      print('THE MENTIONED KEY IS ABSENT IN THE ABOVE DICTIONARY')
has_key(5)
has_key(9)

#Write a python script to merge two python dictionaries.
def Merge(dictx,dicty):
    res = {**dictx, **dicty}
    return res

dict_x = {1:10,2:20}
dict_y = {3:30,4:40}
dict_z = Merge(dict_x,dict_y)
print (dict_z)

#Write a python program to sum all the items in a dictionary.
def Sum(dict):
    sum = 0;
    for i in dict.values():
        sum = sum + i;

    return sum;

Dict = {1:10,2:20,3:30,4:40,5:50}
print("SUM OF ALL THE ITEMS IN THE DICTIONARY IS: ",sum(Dict))

#Write a python script to add a key to a dictionary.
Dict = {1:'a', 2:'B',3:'@',4:40}
Dict[5] = "blue"

print(Dict);

#Write a python script to concatenate following dictionaries to create a new one.
#Sample Dictionary:
#dic1 = {1:10,2:20}
#dic2 = {3:30,4:40}
#dic3 = {5:50,6:60}
#Expected Result: {1:10,2:20,3:30,4:40,5:50,6:60}
dict1 = {1:10,2:20}
dict2 = {3:30,4:40}
dict3 = {5:50,6:60}

def Concate(D1,D2,D3):
    res = {**D1,**D2,**D3}
    return res

print("CONCATED DICTIONARY: ",Concate(dict1,dict2,dict3))
