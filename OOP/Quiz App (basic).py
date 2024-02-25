
#todo question ve quiz isminde class olucak quiz classı questionları alıcak cevapları tutucak en son skor göstercek

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer

class Quiz:
    def __init__(self, question):
        self.question = question
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.question[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru: {self.questionIndex + 1} {question.text}")

        for q in question.choices:
            print("-" + q)
        
        self.guess()

    def guess(self):
        question = self.getQuestion()
        answer = input("cevap: ")

        if question.checkAnswer(answer):
            self.score+=1
        self.questionIndex+=1

        self.loadQuestion()
    
    def loadQuestion(self):
        totalQuestion = len(questions)
        questionNumber = self.questionIndex+1 

        if questionNumber > totalQuestion:
            print("Quiz bitti")
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("Score:",self.score)
    
    def displayProgress(self):
        print(f" Question {self.questionIndex+1} of {len(questions)} ".center(100,"*"))
        

q1 = Question("en iyi programlama dili hangisidir?" , ["C#","python","javascript","java"] , "python")
q2 = Question("en popular programlama dili hangisidir?" , ["python","javascript","C#","java"] , "python")
q3 = Question("en çok kazandıran programlama dili hangisidir?" , ["C#","python","javascript","java","python"] , "python")


questions = [q1,q2,q3]

quiz = Quiz(questions)
# question = Quiz.getQuestion()
quiz.loadQuestion()
# print(quiz.getQuestion().text)


















