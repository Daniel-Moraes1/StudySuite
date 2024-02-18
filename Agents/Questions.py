class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.review = True
    def grade(self, response):
        # do some AI API to check if there is similarity between the response and the answer
        # temporary answer
        correct = self.answer == response
        self.review = not correct
        return correct

# a class API template
class Question_Bank:
    def __init__(self):
        self.questions = []
        self.total = 0
    def generate_questions(self, transcript):
        
    def grade_questions(self, responses):
        grades = []
        for i, response in enumerate(responses):
            grades.append(self.questions[i].grade(response))
        return grades
    

