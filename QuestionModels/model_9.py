# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:52:59 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np




class model_9(MultipleChoice):
    
    TYPE = "multiplechoice_MultiAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs        = [
                        'boolean',
                        ]   

    CHOICES         = [ "A and B are equivalent",
                                   "A and C are equivalent",
                                   "B and C are equivalent",
                                   "None of the expressions are equivalent"]
    QUESTION        = """Considering the following piece of code, select all the true choices.
$$$    
Boolean A = {expression[0]};
Boolean B = {expression[1]};
Boolean C = {expression[2]};
$$$
"""
    shuffle = False       

    def __init__(self):
        BASE_DIR    = os.path.dirname(os.path.dirname(__file__))
        DIR         = os.path.join(BASE_DIR,'data','booleanexpression.json')
        with open(DIR) as f:
            self.booleanList = json.load(f)
            
    def model(self):
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
            
        X['answer'] =  ANSWERs
            
        return X    
    


        
if __name__=="__main__":
    pass
    
