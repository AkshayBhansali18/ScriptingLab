def sequence(str):
    if len(str)==1 and str.isalpha():
        return True
    else:
        if str[0].isalpha():
            return False
        else:
            for i in range(1,len(str)-1):
                if((str[i].isalpha())and not ((str[i-1]=='+' or str[i-1]=='=')and(str[i+1]=='+' or str[i+1]=='='))):
                    return False
            if str[len(str)-1].isalpha():
                return False
            return True
print(sequence("+f++d+"))
