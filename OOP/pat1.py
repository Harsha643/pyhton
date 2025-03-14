
start=1
for i in range(1,6):
    temp=""
    for j in range(0,i):
        
        if i>=j:
            # print(start,end=" ")
            if i%2 != 0:
                temp+=str(start)
            else:
                temp=str(start)+temp
            start+=1
    print(temp)


print("__________________________________")

rows = 8
for h in range(rows):
    for g in range(rows - h - 1):
        print(" ", end="")
    for l in range(rows): 
        print("*", end="")
    print()
