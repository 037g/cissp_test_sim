import json
import random

class QuestionEngine:
	
	def __init__(self, questioncount:int, 
					   jsonfile:str='bank\cissp_questions.json',
					   questionisrandom=True,
					   answerisalpha:bool=True,
					   answerisrandom:bool=True):
		"""Use JSON files to make exams"""
	
		self.correct              = 0
		self.incorrect            = 0
		self.questionNumbers      = []
		self.jsonData             = {}   
		self.totalQuestions       = 0
		self.currentQuestion      = ""
		self.currentAnswers       = {}
		
		self.questionCount        = questioncount
		self.jsonFile             = jsonfile
		self.questionIsRandom     = questionisrandom
		self.answerIsAlpha        = answerisalpha
		self.answerIsRandom       = answerisrandom
		
		self.jsonData             = self.loadJsonFile()
		self.totalQuestions       = len(self.jsonData['questions'])
		self.questionSet          = self.complieQuestions()
		self.totalFromQuestionSet = len(self.questionSet)

		
	def loadJsonFile(self) -> dict:
		"""Load the json question file"""
		
		with open(self.jsonFile) as f:
			self.jsonData = json.load(f)
			
		return self.jsonData 
	
	
	def complieQuestions(self) -> dict:
		"""Create dictionary of questions and question number"""
		
		if self.questionIsRandom:
			questions = random.sample(range(0, self.totalQuestions), 
									  self.questionCount)
		else:
			questions = list(range(0, self.questionCount))
			
		questionSet    = {}
		currentAnswers = {}
		for itr, question in enumerate(questions):
			answers         = self.jsonData['questions'][question]['answers']
			questionSection = self.jsonData['questions'][question]
			answerKeys = '123456789'
			if self.answerIsAlpha:
				answerKeys = 'abcdefghi'

			answerValues = list(answers.keys())
			if self.answerIsRandom:
				random.shuffle(answerValues)
		
			currentAnswers = {}
			for answer in range(len(answerKeys)):
				if answer >= len(answerValues): 
					break
				else:
					currentAnswers.update( { answerKeys[answer]:{
										    answerValues[answer]:answers[answerValues[answer]] } } )
			
				questionSet[itr] = ( { 'question':    questionSection['question'],
								       'answers':      currentAnswers, 
								       'solution':    questionSection['solution'],
									   'explanation': questionSection['explanation'] } )

		return questionSet
	
	
	def getQuestion(self, questionnumber:int) -> str:
		"""Return question from compiled questions"""
		
		return self.questionSet[questionnumber]['question']
		
	
	def getAnswers(self, questionnumber:int) -> dict:
		"""Return dictionary with answers for given question"""
		
		return self.questionSet[questionnumber]['answers']
		
		
	def getSolutionText(self, questionnumber:int) -> str:
		"""Return solution for given question"""
		
		solution     = self.questionSet[questionnumber]['solution']
		answers      = self.questionSet[questionnumber]['answers']
		solutiontext = ""
		if self.answerIsAlpha:
			toconvert = { '1': 'a', '2': 'b', '3': 'c', '4': 'd', 
					      '5': 'e', '6': '7', '7': 'g', '8': 'h', '9': 'i' }
			for key, value in answers.items():
				for k, v in value.items():
					if solution == k:
						solutiontext = v
		#else:
			

		return solutiontext
		
		
	def getExplanation(self, questionnumber:int) -> str:
		"""Return solution for given question"""
		
		return self.questionSet[questionnumer]['explanation']
		

	def setCorrectPlusOne(self) -> None:
		"""Increment correct answer counter by one"""
		
		self.correct += 1
		
		
	def setIncorrectPlusOne(self) -> None:
		"""Increment incorrect counter by  one"""
		
		self.incorrect += 1
		
		
	def getQuestionRemainingCount(self) -> int:
		"""Number of questions that have not been answered"""
		
		return self.totalQuestions - (self.correct + self.incorrect)
		
		
	def getQuestionsAnsweredCount(self) -> int:
		"""Get total of questions answered"""
		
		return self.correct + self.incorrect
		
		
	def compareSolution(self, questionnumber:int, answerguess:int) -> bool:
		"""Compare value to solution"""
		
		if answerguess == self.questionSet[questionnumber]['solution']:
			return True
		else:
			return False
		
			
	