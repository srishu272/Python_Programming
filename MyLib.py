PI = 3.14
info = {"fname": "Srishu","lname" : "Chintakindi", "age" : 19, "city" : "Surat", "CGPA": 9.25}

def sum(a=10, b=20, c=30):
    return a+b+c

def name(fname, lname, mname=""):
    if (mname == ''):
        print(fname+" "+lname)
    else:
        print(fname+" "+mname+" "+lname)
    
