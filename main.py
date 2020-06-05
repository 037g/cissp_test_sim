################################################
# Simple test simulator.
# See README and LICENSE
################################################
#import random
from questengine import QuestionEngine
from helpers import bc, ask, clear

#Main
if __name__ == "__main__":
    qe = QuestionEngine(3)

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

        result = ask(q, qe)
        if result == 'correct':
            print("\n{}Correct!!!\n\n{}".format(bc.OKGREEN, bc.ENDC))
        elif result == 'wrong':
            print("\n{} Wrong!!! The correct Answer is: {}{}\n\n{}".format(bc.WARNING,
                bc.OKGREEN, qe.getSolutionText(q), bc.ENDC))
        elif result == "exit":
            b = True
    
        input("Press ENTER to continue...")

'''
    clear()
    #Display results
    print("Results:")
    print("Questions answered: {} of {}\n".format(totala, num))

    print("Scores from questions answered:")
    print("{}# Right: {} {}% {}".format(bc.OKGREEN, str(right), righta, bc.ENDC))
    print("{}# Wrong: {} {}% \n{}".format(bc.WARNING, str(wrong), wronga, bc.ENDC))

    print("Scores from total questions")
    print("{}# Right: {} {}% {}".format(bc.OKGREEN, str(right), rightq, bc.ENDC))
    print("{}# Wrong: {} {}% {}".format(bc.OKGREEN, str(wrong), wrongq, bc.ENDC))
    print("{}# Skipped: {}\n{}".format(bc.WARNING, skipq, bc.ENDC)) 
'''