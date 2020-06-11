# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:51:33 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np




class model_4(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs = [
                'remainder',
                ]   

    QUESTION   = "Which of the following values results in {value}?"
    CHOICES    = [ "$$${choice[0]}$$$",
                    "$$${choice[1]}$$$",
                    "$$${choice[2]}$$$",
                    "$$${choice[3]}$$$",
                    "$$${choice[4]}$$$"]     
    def model(self):
        X               = {}
        X['choice']     = []
        results = []
        while len(results) < 5:
            c = random.randint(1,9)
            b = random.randint(1,15)
            v = random.randint(1,b)
            a = c * b + v
            if (a%b) not in results:
                X['choice'].append("{0} % {1}".format(a,b))
                results.append(a%b)                
        i               = random.choice(range(len(results)))
        X['value']      = results[i]
        X['answer']     = X['choice'][i]
        
        return X
    


        
if __name__=="__main__":
    pass
    
