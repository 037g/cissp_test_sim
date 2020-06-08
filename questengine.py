import json
import random
from pathlib import Path


class QuestionEngine:

    def __init__(self, jsonfile: str = 'bank/cissp_questions.json',
                 questionisrandom: bool = True,
                 answerisalpha: bool = True,
                 answerisrandom: bool = True):
        """Use JSON files to make exams"""

        self._jsonFile = jsonfile
        self._questionIsRandom = questionisrandom
        self._answerIsAlpha = answerisalpha
        self._answerIsRandom = answerisrandom
        self._jsonData = self.__loadJsonFile()

        self.correct = 0
        self.incorrect = 0
        self.totalQuestions = len(self._jsonData['questions'])
        self.questionSet = self.__complieQuestions()

    def __loadJsonFile(self) -> dict:
        """Load the json question file"""

        jsonDataFile = Path(self._jsonFile)
        with open(jsonDataFile) as f:
            self._jsonData = json.load(f)
        f.close()

        return self._jsonData

    def __complieQuestions(self) -> dict:
        """Create dictionary of questions and question number"""

        if self._questionIsRandom:
            questions = random.sample(range(0, self.totalQuestions),
                                      self.totalQuestions)
        else:
            questions = list(range(0, self.totalQuestions))

        questionSet = {}
        currentAnswers = {}
        for itr, question in enumerate(questions):
            answers = self._jsonData['questions'][question]['answers']
            questionSection = self._jsonData['questions'][question]
            answerKeys = '123456789'
            if self._answerIsAlpha:
                answerKeys = 'abcdefghi'

            answerValues = list(answers.keys())
            if self._answerIsRandom:
                random.shuffle(answerValues)

            currentAnswers = {}
            for answer in range(len(answerKeys)):
                if answer >= len(answerValues):
                    break
                else:
                    currentAnswers.update({answerKeys[answer]: {
                        answerValues[answer]: answers[answerValues[answer]]}})

                questionSet[itr] = ({'question':    questionSection['question'],
                                     'answers':      currentAnswers,
                                     'solution':    questionSection['solution'],
                                     'explanation': questionSection['explanation']})

        return questionSet

    def getQuestion(self, questionnumber: int) -> str:
        """Return question from compiled questions"""

        return self.questionSet[questionnumber]['question']

    def getAnswers(self, questionnumber: int) -> dict:
        """Return dictionary with answers for given question"""

        return self.questionSet[questionnumber]['answers']

    def getExplanation(self, questionnumber: int) -> str:
        """Return solution for given question"""

        return self.questionSet[questionnumber]['explanation']

    def getSolutionText(self, questionnumber: int) -> str:
        """Return solution for given question"""

        solution = self.questionSet[questionnumber]['solution']
        answers = self.questionSet[questionnumber]['answers']
        solutiontext = ""
        for key, value in answers.items():
            for k, v in value.items():
                if solution == k:
                    solutiontext = v

        return solutiontext

    def compareSolution(self, questionnumber: int, answerguess: int) -> bool:
        """Compare value to solution"""

        if answerguess == self.questionSet[questionnumber]['solution']:
            return True
        else:
            return False
