testcases=int(input())
i=1
while(testcases>0):
    N=input()
    visitors=[int(visitors) for visitors in input().split()]
    records=0
    j=0
    record=0
    while(j<(len(visitors))):
        greaterthanpreviousday=((j==0) or (visitors[j]>record))
        greaterthanfollowingday=((j==(len(visitors)-1)) or (visitors[j]>visitors[j+1]))
        if(greaterthanpreviousday and greaterthanfollowingday):
            records=records+1
        record=max(record, visitors[j])
        j=j+1
    print("Case #"+str(i)+':', records)
    testcases=testcases-1
    i=i+1
