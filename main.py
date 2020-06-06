################################################
# Simple test simulator.
# See README and LICENSE
################################################
from questengine import QuestionEngine
from helpers import bc, ask, clear

# Main
if __name__ == "__main__":
    qe = QuestionEngine()
    qc = 0

    clear()
    while True:
        qc = input("How many questions do you want to practice? 1-{} (X to exit): \n"
                   .format(qe.totalQuestions))
        if qc == "x" or qc == "X":
            exit()
        elif qc.isdigit() and (int(qc) > 0
                               and int(qc) <= qe.totalQuestions):
            break
        else:
            clear()

    i = 0
    is_done = False
    result = None
    while True:
        try:
            qn = i + 1
            clear()
            print("Question {} of {} (X to exit)\n".format(qn, qc))

            result = ask(i, qe)
            if result == 'correct':
                qe.correct += 1
                i += 1
                print("\n{}Correct!!! The Answer is: {}\n\n{}".format(bc.OKGREEN, qe.getSolutionText(i - 1), bc.ENDC))
            elif result == 'wrong':
                qe.incorrect += 1
                i += 1
                print("\n{} Wrong!!! The correct Answer is: {}{}\n\n{}".format(bc.WARNING,
                                                                               bc.OKGREEN, qe.getSolutionText(i - 1), bc.ENDC))
            elif result == "exit":
                qn = qc

            if int(qn) == int(qc):
                raise Exception()
            else:
                input("Press ENTER to continue...")

        except Exception as e:
            if int(qn) == int(qc):
                input("Press ENTER to view results...")
                break
            else:
                pass

    clear()
    answered = qe.correct + qe.incorrect
    right = qe.correct
    wrong = qe.incorrect
    if answered == 0:
        righta = "0.0"
        wronga = "0.0"
    else:
        righta = int(right) / int(answered) * 100
        wronga = wrong / int(answered) * 100
    rightq = int(right) / int(qc) * 100
    wrongq = wrong / int(qc) * 100
    skipq = int(qc) - int(answered)
    print("Results:")
    print("Questions answered: {} of {}\n".format(answered, qc))

    print("Scores from questions answered:")
    print("{}# Right: {} {}% {}".format(
        bc.OKGREEN, str(right), righta, bc.ENDC))
    print("{}# Wrong: {} {}% \n{}".format(
        bc.WARNING, str(wrong), wronga, bc.ENDC))

    print("Scores from total questions")
    print("{}# Right: {} {}% {}".format(
        bc.OKGREEN, str(right), rightq, bc.ENDC))
    print("{}# Wrong: {} {}% {}".format(
        bc.WARNING, str(wrong), wrongq, bc.ENDC))
    print("{}# Skipped: {}\n{}".format(bc.WARNING, skipq, bc.ENDC))
