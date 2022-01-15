#Write a Python  program to add member(s) in a set and clear a set
set_a = {"apple", "blue", "red"}
set_elements = [1,10]
set_a.add("orange")
print("Adding one element:")
print(set_a)
set_a.update(set_elements)
print("Adding more than one element:")
print(set_a)
print("Clearing the set:")
set_a.clear()
print(set_a)

#Write a python program to remove an item from a set if it is present in the set
set_b = {"C","C++","Java","Python","SQL"}
set_b.discard("a")
set_b.discard("C")
print(set_b)

#Write a python program to create an intersection, union, difference of sets
set_c1 = {"a","BAT","c","Zebra"}
set_c2 = {"a","z","CAT"}
print("INTERSECTION OF SETS:", set_c1.intersection(set_c2))
print("UNION OF SETS: ",set_c1.union(set_c2))
print("DIFFERENCE OF SETS: ",set_c1.difference(set_c2))

#Write a python program to find maximum and minimun values in the set
set_d = {1,3,45,678,90.87}
print("MAXIMUM VALUE OS THE SET: ", max(set_d))
print("MINIMUN VALUE OF THE SET: ", min(set_d))

#Write a python program to find the most common elements and their counts from list, tuple, dictionary.
#1 Most commo element from set.
Mylist = [1,2,3,4,3,2]
Mylist2 = list(set(Mylist))

MaxNo = 0
Maxvalue = list([])

i = 0
while i < len(Mylist2) :
    if Mylist.count(Mylist2[i]) > MaxNo :
        MaxNo = Mylist.count(Mylist2[i])
    i += 1

i = 0
while i < len(Mylist2) :
    if Mylist.count(Mylist2[i]) == MaxNo :
        Maxvalue.append(Mylist2[i])
    i += 1

print("\n")
i = 0
while i < len(Maxvalue) :
    print(f"{Maxvalue[i]} is repeated {MaxNo} times in List\n")
    i += 1

#2 Most common elements from tuple
MyTuple = (1,2,3,3,4,2,1)

Mylist = list(MyTuple)
Mylist2 = list(set(Mylist))

MaxNo = 0
Maxvalue = list([])

i = 0
while i < len(Mylist2) :
    if Mylist.count(Mylist2[i]) > MaxNo :
        MaxNo = Mylist.count(Mylist2[i])
    i += 1

i = 0
while i < len(Mylist2) :
    if Mylist.count(Mylist2[i]) == MaxNo :
        Maxvalue.append(Mylist2[i])
    i += 1


print("\n")
i = 0
while i < len(Maxvalue) :
    print(f"{Maxvalue[i]} is repeated {MaxNo} times in Tuple\n")
    i += 1

#3 Most common element in dictionary
Dic = {1:10 , 2:30 , 3:60 , 4:60 , 5:50 , 6:60}

Mylist = list(Dic.values())
Mylist2 = list(set(Mylist)) 

MaxNo = 0
Maxvalue = list([])

i = 0
while i < len(Mylist2) :
    if Mylist.count(Mylist2[i]) > MaxNo :
        MaxNo = Mylist.count(Mylist2[i])
    i += 1

i = 0
while i < len(Mylist2) :
    if Mylist.count(Mylist2[i]) == MaxNo :
        Maxvalue.append(Mylist2[i])
    i += 1

print("\n")
i = 0
while i < len(Maxvalue) :
    print(f"{Maxvalue[i]} is repeated {MaxNo} times in Dictionary\n")
    i += 1

    