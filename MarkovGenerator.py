import random

EOS = ['.', '?', '!']

class MarkovGenerator(object):

	def __init__(self, textFile, chainSize = 2):
		self.textFile = textFile
		self.chainSize = chainSize
		self.dictionary = {}
		self.wordList = self.textToWords()
		self.buildDictionary()
	
	# Convert open text file to word tokens.
	def textToWords(self):
		
		self.textFile.seek(0)
		text = self.textFile.read()
		wordList = text.split()
		return wordList

	# Build dictionary of words.
	def buildDictionary(self):
		
		if (len(self.wordList) < self.chainSize):
			return
		
		for i in range(len(self.wordList) - self.chainSize - 1):
			chain = []
			for j in range(0, self.chainSize):
				chain.append(self.wordList[i + j])
				lastWord = self.wordList[i + j + 1]
			key = tuple(chain)
			if key not in self.dictionary:
				self.dictionary[key] = []
			self.dictionary[key].append(lastWord)
	
	# Generate strings of words.
	# Can input word count of generated string (default 10).
	def generateText(self, textSize = 10):
		
		seedNumber = random.randint(0, len(self.wordList) - self.chainSize)
		string = []
		seedWords = []
		for j in range(0, self.chainSize):
			seedWords.append(self.wordList[seedNumber + j])
		string.extend(seedWords)
		
		for i in range(textSize):
			if (self.chainSize - 1 <= 1):
				lastWordLength = 2
			else:
				lastWordLength = self.chainSize - 1
			lastWords = string[-1 * lastWordLength:]
			next = random.choice(self.dictionary[tuple(lastWords)])
			if (next[-1] in EOS):
				string.append(next)
				break
			string.append(next)

		string[0] = string[0].title()

		return ' '.join(string)
		
		
		
		
		
		
