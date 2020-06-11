# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:52:37 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np



class model_8(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs        = [
                        'boolean',
                        ]   

    CHOICES         = [ "$$${choice[0]}$$$",
                    "$$${choice[1]}$$$",
                    "$$${choice[2]}$$$",
                    "$$${choice[3]}$$$"]
    QUESTION        = "The expression $$${expression}$$$ is equivalent to"
    
    def __init__(self):
        BASE_DIR    = os.path.dirname(os.path.dirname(__file__))
        DIR         = os.path.join(BASE_DIR,'data','booleanexpression.json')
        with open(DIR) as f:
            self.booleanList = json.load(f)
            
            
    def model(self):
        X           = {}
        i           = random.choice(['1','2'])
        X['expression'] , X['choice'] = random.sample(self.booleanList[i],2)
        X['choice'] = [X['choice']]
        X['choice'].extend(random.sample(self.booleanList['-' + i],3))
        X['answer'] = X['choice'][0]
        return X
    



        
if __name__=="__main__":
    pass
    
