def OddRange(num1,num2):
    my_list=[]
    for i in range(num1,num2):
        if(not i%2==0):
            my_list.append(i)
    return my_list
new_list=OddRange(3,10)
print(new_list)

