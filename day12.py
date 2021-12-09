class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
        
    def calculate(self):
        score = 0
        for i in range(len(scores)):
            score += scores[i]
        average = score / len(scores)
        if average >= 90:
            grade = 'O'
        elif average < 90 and average >= 80:
            grade = 'E'
        elif average < 80 and average >= 70:
            grade = 'A'
        elif average < 70 and average >= 55:
            grade = 'P'
        elif average < 55 and average >= 40:
            grade = 'D'
        else:
            grade = 'T'
        return grade

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
