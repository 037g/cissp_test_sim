from os import system, name
from questengine import QuestionEngine

#Alias colos
class bc:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

#Ask question
def ask(question_num: int, questionset:QuestionEngine) -> str:
    """Ask user question from dataset"""
	
    question    = questionset.getQuestion(question_num)
    answers     = questionset.getAnswers(question_num)
    solution    = questionset.getSolutionText(question_num)
    answertable = {}
    print("{}".format(question))
    for key, val in answers.items():
        for k, v in val.items():    		 
            print(" {}. {}".format(key, v))
            answertable[key] = k
	
    reply = input("\n{}Your Answer: {}".format(bc.OKBLUE, bc.ENDC))
    reply = reply.lower()
    if questionset.compareSolution(question_num, answertable[reply]):
        return 'correct'
    else:
        return 'wrong'
    
    if reply == "x":
        return "exit"
    else:
        return "error"
	
#Clear screen
def clear() -> None:
    """Clear the screen"""
    if name == "posix":
        _ = system("clear")
    else:
        _ = system('cls')