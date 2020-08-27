testcases=int(input())
j=1
while(testcases>0):
    array_length, required_countdown_length=[int(x) for x in input().split()]
    array=[int(array) for array in input().split()]
    countdown_length=0
    number_of_countdowns=0
    i=1
    while(i<len(array)):
        if(array[i]==(array[i-1]-1)):
            countdown_length=countdown_length+1
        else:
            countdown_length=0
        if(array[i]==1 and countdown_length>=(required_countdown_length-1)):
                number_of_countdowns=number_of_countdowns+1
        i=i+1
            
    print("Case #"+str(j)+':',number_of_countdowns)
    testcases=testcases-1
    j=j+1
