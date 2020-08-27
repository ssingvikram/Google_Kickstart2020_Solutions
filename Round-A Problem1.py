testcases=input()
testcases=int(testcases)

i=0
j=0
total_cost=0
number_of_flats=0

while j<testcases:
    flats, budget=input().split()
    budget=int(budget)
    costs=list(map(int, input().split()))
    costs.sort()
    while(total_cost<budget):
        if(i==len(costs)):
            break
        else:
            total_cost=total_cost+costs[i]
            if(total_cost<=budget):
                number_of_flats=number_of_flats+1
            else:
                break
        i=i+1
    print('Case #'+str(j+1)+':',number_of_flats)
    i=0
    total_cost=0
    number_of_flats=0
    j=j+1
