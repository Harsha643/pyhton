import random
import time
 
guess=int(input("what is your guess ? : "))
 
correct_number = random.randint(1,100)
guess_count=1
while guess!=correct_number:
    guess_count+=1
    if guess<correct_number:
        time.sleep(2)
        guess=int(input("you need to guess higher ,what is your guess? : "))
    else:
        time.sleep(2)
        guess=int(input("you need to guess lower ,what is your guess? : "))

print(f"you got the {correct_number} in {guess_count} attempt")