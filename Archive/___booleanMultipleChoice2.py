


import random
import json
import os



class booleanMultipleChoice2:
    def __init__(self):
        self.BASE_DIR    = os.path.dirname(os.path.dirname(__file__))
        self.DIR         = os.path.join(self.BASE_DIR,'data','booleanexpression.json')
        with open(self.DIR) as f:
            self.booleanList = json.load(f)

        self.CHOICES        = [ "A and B are equivalent",
                                   "A and C are equivalent",
                                   "B and C are equivalent",
                                   "None of the expressions are equivalent"]
        self.QUESTION       = """Considering the following piece of code, select all the true choices.
Boolean A = {expression[0]};
Boolean B = {expression[1]};
Boolean C = {expression[2]};
"""


    def generate(self):
        X               = {}
        temp            = random.choice(['1','2'])        
        X['expression'] = random.sample(self.booleanList[temp] ,2)
        X['expression'].append(random.choice(self.booleanList['-' + temp]))
        random.shuffle(X['expression'])
        ANSWERs = []
        for i in range(len(X['expression'])):
            for j in range(i+1,len(X['expression'])):
                if (X['expression'][i] in self.booleanList[temp]) and \
                    (X['expression'][j] in self.booleanList[temp]):
                        ANSWERs.append(True)
                else:
                    ANSWERs.append(False)
        if True in ANSWERs:
            ANSWERs.append(False)
        else:
            ANSWERs.append(True)
        
        print(self.QUESTION.format(**X))
        for CHOICE in self.CHOICES: print(". ",CHOICE.format(**X))
        print("Answer: ",ANSWERs)
        
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                ANSWERs]


           
if __name__=="__main__":
    
    booleanmultiplechoice = booleanMultipleChoice2()
    _ = booleanmultiplechoice.generate()
