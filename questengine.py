import json
import random
from string import ascii_lowercase

class QuestEngine:
	
	def __init__(self, jsonfile:str, questioncount:int):
		"""Use JSON files to make exams"""
	
		self.correct               = 0
		self.incorrect             = 0
		self.questionNumbers       = []
		self.jsonData              = {}
		self.totalQuestions        = 0
		
		with open(jsonfile) as f:
			self.jsonData = json.load(f)
		self.totalQuestions = len(self.jsonData['questions'])
			
		try:
			questions = random.sample(range(0, self.totalQuestions), questioncount)
			for question in questions:
				self.questionNumbers.append(question)
				
		except:
			print('Invalid input')
			exit()
		
		
	def correctPlusOne(self) -> None:
		"""Increment correct answer counter by one"""
		
		self.correct += 1
		
		
	def incorrectPlusOne(self) -> None:
		"""Increment incorrect counter by  one"""
		
		self.incorrect +=1
		

	def showQuestion(self, questionnumber:int) -> int:
		"""Display question with answer placement randomized"""

		try:
			questionNumber = self.questionNumbers[questionnumber]
			question       = self.jsonData['questions'][questionNumber]['question']
			answers        = self.jsonData['questions'][questionNumber]['answers']
			solution       = self.jsonData['questions'][questionNumber]['solution']
			answerLetter   = ascii_lowercase 
			
			answerkeys = list(answers.keys())
			random.shuffle(answerkeys)
			print("{}. {}".format(questionnumber + 1, question))
			for itr, answer in enumerate(answerkeys):
				print("	{}. {}".format(answerLetter[itr], answers[answer]))
			
			return solution
			
		except IndexError:
			print('Invalid Input')
			exit()

numberOfQuestions = 3
qe = QuestEngine('bank\cissp_questions.json', numberOfQuestions)

for n in range(0, numberOfQuestions):
	qe.showQuestion(n)
