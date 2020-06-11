


import random
import json
import os


class booleanMultipleChoice:
    def __init__(self):
        BASE_DIR    = os.path.dirname(os.path.dirname(__file__))
        DIR         = os.path.join(BASE_DIR,'data','booleanexpression.json')
        with open(DIR) as f:
            self.booleanList = json.load(f)
        
        self.CHOICES        = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
        self.QUESTION       = "The expression {expression} is equivalent to"
        self.ANSWER         = "{answer}"        

    def generate(self):
        X = self.generateQuestion()
        """replace X inside the Qestion and Choices and then print them """
        print('\n')
        print(self.QUESTION.format(**X))
        for i in self.CHOICES: 
            print(". ",i.format(**X))
        print("\nAnswer: ", self.ANSWER.format(**X))
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]

    def generateQuestion(self):
        X    = {}
        i    = random.choice(['1','2'])
        X['expression'] , X['choice'] = random.sample(self.booleanList[i],2)
        X['choice'] = [X['choice']]
        X['choice'].extend(random.sample(self.booleanList['-' + i],3))
        X['answer'] = X['choice'][0]
        return X


           
if __name__=="__main__":
    

    booleanmultiplechoice = booleanMultipleChoice()
    _ = booleanmultiplechoice.generate()

