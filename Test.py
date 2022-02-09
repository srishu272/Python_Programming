from calendar import c
from MyLib import PI, info,sum as Add, name as N

def Area():
    print("AREA: ",(PI*10*10))

Area()
print("INFO DICTIONARY: ",(info))
print("FUN using Positional parameters:",(Add(b=1, c=10, a=19)))
print("FUN using Default parameters:",(Add()))
N(lname="Chintakindi", fname="Srishu")
N(lname="Chintakindi", mname="Ashok",fname="Srishu")

