# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:58:38 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np


class model_21(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
    
    QUESTION        = "If x= {x}, which of the following statement is true? Select all that apply."
    shuffle = True
    
    def __init__(self):
        BASE_DIR    = os.path.dirname(os.path.dirname(__file__))
        DIR         = os.path.join(BASE_DIR,'data','booleanexpression.json')
        with open(DIR) as f:
            self.booleanList = json.load(f)
            
    def model(self):
        X = {}
        statements      = self.booleanList["1"] + self.booleanList["2"]
        statements     += ['x > y','x >= y','x < y','x < y']
        X['choice']     = []
        X['answer']     = []
        X['x']          = random.randint(0,30)
        for i in range(4):
            [s1,s2]     = random.sample(statements,k=2)
            x           = X['x']
            s1          = s1.replace("y",str(random.randint(0,30)))
            s2          = s2.replace("y",str(random.randint(0,30)))
            X['choice'].append("(%s) is same as (%s)"%(s1,s2))
            s1      = s1.replace("!(","not(").replace("&&","&").replace("||","|")
            s2      = s1.replace("!(","not(").replace("&&","&").replace("||","|")
            X['answer'].append(eval(s1) == eval(s2))          

        return X   



        
if __name__=="__main__":
    pass
    
