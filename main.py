################################################
# Simple test simulator.
# See README and LICENSE
################################################
import random
from questions_answers import questions, answers
from os import system, name

#Alias colos
class bc:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

#Tally results
right  = 0
wrong  = 0
num    = 0
totala = 0
totalq = 0

#Clear screen
def clear() -> None:
    """Clear the screen"""
    if name == "posix":
        _ = system("clear")
    else:
        _ = system('cls')

#Ask question
def ask(question_num: int) -> str:
    """Takes a random question key from the dictionary to ask the user"""

    print(questions[question_num])
    print("(X to exit)")
    reply = input("{}Your Answer: {}".format(bc.OKBLUE, bc.ENDC))
    reply = reply.upper()
    if reply in ["A", "B", "C", "D", "E", "F", "G"]:
        if reply == answers[question_num]:
            return "correct"
        else:
            return "wrong"
    if reply == "X":
        return "exit"
    else:
        return "error"

#Main
if __name__ == "__main__":
    #If all else fails, repeat
    q = []
    clear()
    while True:
        num = input("How many questions do you want to practice? 1-250 (X to exit): \n")
        if num.isdigit():
            num = int(int(num.strip()))
            if num > 0 and num < 251:
                q = random.sample(questions.keys(), num)
                break
            else:
                clear()
        else:
            clear()
            if num == "x" or num == "X":
                exit()

    i = 0
    b = False
    l = len(q)
    #Don't repeat questions
    while True:
        if b == True or i+1 > l:
            break

        v = q[i]
        clear()
        print("Question {} of {}".format(i+1, l))
        result = ask(v)
        if result == "correct":
            right  += 1
            totala += 1
            i      += 1
            print("\n{}Correct!!!\n\n{}".format(bc.OKGREEN, bc.ENDC))
        elif result == "wrong":
            wrong  += 1
            totala += 1
            i      += 1
            print("\n{} Wrong!!! The correct Answer is {}{}\n\n{}".format(bc.WARNING,
                bc.OKGREEN,answers[v], bc.ENDC))
        elif result == "exit":
            b = True
            break
        else:
           continue 

        input("Press ENTER to continue...")


    if totala == 0:
        righta = "0.0"
        wronga = "0.0"
    else:
        righta = str(right/totala * 100)
        wronga = str(wrong/totala * 100)
    rightq = str(right/num * 100)
    wrongq = str(wrong/num * 100)
    skipq  = str(num-totala)

    clear()
    #Display results
    print("Results:")
    print("Questions answered: {} of {}\n".format(totala,num))

    print("Scores from questions answered:")
    print("{}# Right: {} {}% {}".format(bc.OKGREEN, str(right), righta, bc.ENDC))
    print("{}# Wrong: {} {}% \n{}".format(bc.WARNING, str(wrong), wronga, bc.ENDC))

    print("Scores from total questions")
    print("{}# Right: {} {}% {}".format(bc.OKGREEN, str(right), rightq, bc.ENDC))
    print("{}# Wrong: {} {}% {}".format(bc.OKGREEN, str(wrong), wrongq, bc.ENDC))
    print("{}# Skipped: {}\n{}".format(bc.WARNING, skipq, bc.ENDC)) 
