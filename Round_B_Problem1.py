testcases=int(input())
i=1
while(testcases>0):
    N=input()
    heights=[int(heights) for heights in input().split()]
    peaks=0
    j=1
    while(j<=(len(heights)-2)):
        if((heights[j]>heights[j-1])and(heights[j]>heights[j+1])):
            peaks=peaks+1
        j=j+1
    print("Case #"+str(i)+':', peaks)
    testcases=testcases-1
    i=i+1
