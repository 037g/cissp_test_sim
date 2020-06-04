################################################
# Simple test simulator.
# See README and LICENSE
################################################
#import random
from questengine import QuestionEngine
from helpers import bc, clear

#New question set
qe = QuestionEngine(3)
num  = 0

#Ask question
def ask(question_num: int) -> str:
    """Ask user question from dataset"""

    question    = qe.getQuestion(question_num)
    answers     = qe.getAnswer(question_num)
    answertable = {}
    print("{}".format(question))
    for key, val in answers.items():
        for k, v in val.items():    		 
            print(" {}. {}".format(key, v))
            answertable[key] = k
						
    reply = input("\n{}Your Answer: {}".format(bc.OKBLUE, bc.ENDC))
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
    clear()
    while True:
        num = input("How many questions do you want to practice? 1-{} (X to exit): \n"
		     .format(qe.totalQuestions))
        if num == "x" or num == "X":
            exit()
        elif num.isdigit() and (int(num) > 0 
		                   and  int(num) <= qe.totalQuestions):
            break
        else:
            clear()
		
    for q in range(0, int(num)):
        clear()
        print("Question {} of {} (X to exit)\n".format(q + 1, qe.totalQuestions))
        ask(q)

'''
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
'''