import time

correct_answer=0
question=input("This is a quiz with five questions. If you answer all five correctly, you win 50,000 rupees. If you answer three or four questions correctly, you win 30,000 rupees. Otherwise, you lose. Are you ready to play? yes or no  : ").lower()
qs=0
if question == "yes":
    question=input("Would you prefer a math quiz or a science quiz?")
    if question=="math":
        qs+=1
        time.sleep(2)
        maths=int(input("What is 7 multiplied by 8?="))
        if maths==56:
            correct_answer+=1
            time.sleep(2)
            maths=int(input("If a train travels 120 miles in 2 hours, what is its average speed? :"))
        else:
            qs+=1
            time.sleep(2)
            maths=int(input("If a train travels 120 miles in 2 hours, what is its average speed? :"))
        if maths== 60:
            qs+=1
            correct_answer+=1
            time.sleep(2)
            maths=int(input("What is the next prime number after 23?"))
        else:
            qs+=1
            time.sleep(2)
            maths=int(input("What is the next prime number after 23?"))

        if maths== 29:
            qs+=1
            correct_answer+=1
            time.sleep(2)
            maths=input("What is the derivative of x^3 + 2x^2 - 5x + 1?")
        else: 
            qs+=1
            time.sleep(2)
            maths=input("What is the derivative of x^3 + 2x^2 - 5x + 1?")
        if maths=="3x^2+4x-5":
            qs+=1
            correct_answer+=1
            time.sleep(2)
            maths=int(input("If you have 10 apples and you take away 3, how many apples do you have?"))
        else:
            qs+=1
            time.sleep(2)
            maths=int(input("If you have 10 apples and you take away 3, how many apples do you have?"))
        if maths==3:
            qs+=1
            correct_answer+=1
            time.sleep(2)
            if qs==5:
                if correct_answer <3:
                    time.sleep(2)
                    print(f"Try again next time  correct answers are {correct_answer}")
                elif correct_answer == 3 or correct_answer==4:
                    time.sleep(2)
                    print(f"you won the 30000 rupees! correct answers are {correct_answer} ")
                else:
                    time.sleep(2)
                    print(f"you won the 50000 rupees! correct answers are {correct_answer} ")
        else:
            if qs==5:
                if correct_answer <3 or correct_answer==0:
                    time.sleep(2)
                    print(f"try again next time  correct answers are {correct_answer} ")
                elif correct_answer == 3 or correct_answer== 4:
                    time.sleep(2)
                    print(f"you won the 30000 rupees  correct answers are {correct_answer}")
                else:
                    time.sleep(2)
                    print(f"you won the 50000 rupees  correct answers are {correct_answer}")


            
    elif question=="science":
        
        if question=="science":
            time.sleep(2)
            qs+=1
            science=input("Question : What is the chemical symbol for water? answer must be like CO2 :")
        if science=="H2O":
            time.sleep(2)
      
            correct_answer+=1
            science=int(input("Question : What is the atomic number of oxygen?:"))
        else:
            qs+=1
            time.sleep(2)
            science=int(input("Question : What is the atomic number of oxygen?:"))
        if science==8 or science=="8":
            qs+=1
            time.sleep(2)
            correct_answer+=1
            science=input("This answer must be separated by commas:  Question :  What are the three states of matter? This answer must be separated by commas: ").lower()
        else:
            qs+=1
            time.sleep(2)
            science=input("This answer must be separated by commas:  Question :  What are the three states of matter? This answer must be separated by commas: ").lower()

        if science== "solid,liquid,gas":
            
            qs+=1
            time.sleep(2)
            correct_answer+=1
            science=input("Question : What is the powerhouse of the cell? :" ).lower()
        else:
            qs+=1
            time.sleep(2)
            science=input("Question : What is the powerhouse of the cell? :" ).lower()
            
        if science=="mitochondria":
            qs+=1
            time.sleep(2)
            correct_answer+=1
            science=input("Question : What is the largest planet in our solar system?  :").lower()
        else: 
            qs+=1
            time.sleep(2)
            science=input("Question : What is the largest planet in our solar system?  :").lower()

        if science=="jupiter":
            qs+=1
            correct_answer+=1
            if qs==5:
                if correct_answer <3:
                    time.sleep(2)
                    print(f"Try again next time  correct answers are {correct_answer}")
                elif correct_answer == 3 or correct_answer==4:
                    time.sleep(2)
                    print(f"you won the 30000 rupees! correct answers are {correct_answer} ")
                else:
                    time.sleep(2)
                    print(f"you won the 50000 rupees! correct answers are {correct_answer}")
        else:
            if qs==5:
                if correct_answer <3:
                    time.sleep(2)
                    print(f"try again next time  correct answers are {correct_answer} ")
                elif correct_answer == 3 or correct_answer== 4:
                    time.sleep(2)
                    print(f"you won the 30000 rupees correct answers are {correct_answer} ")
                else:
                    time.sleep(2)
                    print(f"you won the 50000 rupees correct answers are {correct_answer} ")

