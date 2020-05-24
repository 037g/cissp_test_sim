import random
from questions_answers import questions, answers


class bc:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'


def ask(question_num: int) -> str:
    """Takes a random question key from the dictionary to ask the user"""

    print(questions[question_num])
    reply = input(bc.OKBLUE + "Your Answer: " + bc.ENDC)
    reply = reply.upper()
    if reply in ["A", "B", "C", "D", "E", "F", "G"]:
        if reply == answers[question_num]:
            return "correct"
        else:
            return "wrong"
    else:
        return "error"


right = 0
wrong = 0

if __name__ == "__main__":
    num = input("How many questions do you want to practice? 1-251: \n")
    num = int(int(num.strip()))
    print("\n\n")
    if num > 0 and num <= 251:
        for i in range(0, num):
            n = random.choice(list(questions.keys()))
            result = ask(n)
            if result == "correct":
                right += 1
                print(bc.OKGREEN + "\nCorrect!!!\n\n" + bc.ENDC)
            elif result == "wrong":
                wrong += 1
                print(bc.WARNING + "\n Wrong!!! The correct Answer is " + bc.OKGREEN +
                      answers[n] + "\n\n" + bc.ENDC)
            else:
                print("Incorrect input. Try again")
                continue
    else:
        print(bc.WARNING + "There are not that many questions." + bc.ENDC)
    print("Results: \n")
    print(bc.OKGREEN + "# Right: " + str(right) + " " +
          str(right/num * 100) + "% " + bc.ENDC + "\n")
    print(bc.WARNING + "# Wrong: " + str(wrong) + " " +
          str(wrong/num * 100) + "% " + bc.ENDC + "\n")
