class sanctionScreening:
	def __init__(self, sanctionList, userInput):
		self.sanctionList = sanctionList
		self.userInput = userInput

	#Outputs hit or not hit results
	def outputResults(self, hit):
		#If Hit is in the list it will output hit
		if hit == True:
			print("Hit")
		else:
			print("No hit")

	#Removes all the spaces of the names from sanction list
	def splitSanctionName(self, name):
		nameArr = []
		for char in name:
			nameArr.append(char.lower())
			nameArr = list(filter(str.strip, nameArr))
		return nameArr

	#This matching algorithm checks if there is any letter difference
	#between the name entered and the sanction name and records how many
	def match(self):
		userInput = self.userInput.replace(" ", "")

		userInputList = []
		hit = False
		for char in userInput:
			userInputList.append(char.lower())

		#Checks against all the sanction names in the sanction list
		for i in range(len(self.sanctionList)):
			sanctionNameArr = self.splitSanctionName(self.sanctionList[i])
			noMatch = 0
			#Compares user input with sanction list name to  see how many
			#letters are different and keeps track of them on noMatch variable
			for x, y in zip(userInputList, sanctionNameArr):
				if x == y:
					pass
				else:
					noMatch += 1

			#Works out the percentage of match from the  name user entered against the names in
			#the sanction list
			percentage = (len(userInputList) - noMatch)/len(userInputList) * 100
			#If the name match percentage is 75% and above or 100% match it will set
			#hit to True
			if noMatch != 0 and percentage >= 75 or noMatch == 0 and percentage == 100:
				hit = True

		self.outputResults(hit)

userInput = input("Enter the name you want to run a check on: ")
sanctionList = sanctionScreening(["Kristopher Doe", "Iceland", "Royal Arctic Line"], userInput)
sanctionList.match()

