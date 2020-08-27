t=int(input())
i=1
while(t>0):
    n=int(input())
    arr=[int(x) for x in input().split()]
    j=0;
    maxlength=0
    while(j<len(arr)-1):
        k=j+1
        currentlength=0
        diff=arr[k]-arr[j]
        while(k<len(arr)):
            if(arr[k]-arr[k-1]==diff):
                currentlength=currentlength+1
            else:
                break
            k=k+1
        if(currentlength>maxlength):
            maxlength=currentlength
        j=k-1
    print('Case #'+str(i)+':', maxlength+1)
    i=i+1
    t=t-1
