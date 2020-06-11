# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:54:10 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np





class model_12(NamingConvention):
    
    TYPE = "multiplechoice_MultiAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs        = [
                        'NamingConvention',
                        ]   

    CHOICES         = [ "{choice[0]}",
                          "{choice[1]}",
                          "{choice[2]}",
                          "{choice[3]}"]
    
    QUESTION        = "According to Java naming convention, \
which of the following names can be {identifier}?"
    shuffle = False
    def model(self):
        X               = {} 
        X['choice']     = []
        X['answer']     = []
        X['identifier'] = random.choice(['class','variable','method'])
        if X['identifier'] == "class":
            for i in range(4):
                choice, answer  = self.generateClass()
                X['choice'].append(choice)
                X['answer'].append(answer)
        elif X['identifier'] == "variable":
            for i in range(4):
                choice, answer  = self.generateVariable()
                X['choice'].append(choice)
                X['answer'].append(answer)
        else:
            for i in range(4):
                choice, answer  = self.generateMethod()
                X['choice'].append(choice)
                X['answer'].append(answer)                

        return X    

        
if __name__=="__main__":
    pass
    
