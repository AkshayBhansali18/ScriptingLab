def charstring(str):
    new_str=[]
    for i in  str:
            num=ord(i)
            val = chr(ord(i) + 1)
            orig=i
            if num>=65 and num<=122:
                val= val.lower()
                if(val in ['a','e','i','o','u']):
                    val=val.upper()
                new_str.append(val)
            else:
                new_str.append(i)
    for i in new_str:
        print(i,end="")
string=input("Enter a string")
charstring(string)


