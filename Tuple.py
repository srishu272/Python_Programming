#Write a python program to create a tuple with differet datatypes.
tuple_a = ("This is tuple", 'a', 2.9065,2000)
print (tuple_a)
print (type(tuple_a))

#Write a python program to create a tuple with numbers and print one item.
tuple_b = (1,20,300,4000,50000)
print(tuple_b[3])

#Write a python program to add an item in a tuple.
tuple_c = ('a', "ABC", 35)
tuple_c = tuple_c + (20,False)
print (tuple_c)

#Write a Python program to convert a tuple to a string.
def toString(Tuple):
    str =''
    for item in Tuple:
        str = str + item
    return str

tuple_d = ('a','BALL','C','dig')
print(toString(tuple_d))

#Write a Python program to find the length of the tuple.
tuple_e = ('apple', 12, 34.0098, True, 'z')
print(len(tuple_e))