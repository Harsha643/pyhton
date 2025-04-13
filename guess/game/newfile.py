import random
countA=0
trun=1
countB=0
roll=random.randint(1,6)

if roll==6 or roll==1:
    countA+=2
    roll=random.randint(1,6)
    countA+=roll
    if roll==6:
        roll=random.randint(1,6)
        countA+=roll
    if roll!=6:
        countA+=roll
    else:
        roll=random.randint(1,6)
        if roll==6 or roll==1:
            countB+=2
            roll=random.randint(1,6)
            countB+=roll
        if roll==6:
            roll=random.randint(1,6)
            countB+=roll
        if roll!=6:
            countB+=roll




    

    
    