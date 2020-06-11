# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:59:41 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np



class model_24(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
    
    QUESTION        = """Which of the following is the correct expression that \
evaluates to true if the integer x is between {lower} and {upper}. Select all that apply."""

    shuffle = False
    def model(self):
        X               = {} 
          
        statements      = ['x > y', 'x > z','x >= y', 'x >= z']        
        statements     += ['x > y || x > z','x > y && x > z']
        X['choice']     = []
        X['answer']     = []
        X['lower']      = random.randint(0,100)
        X['upper']      = random.randint(X['lower'],100)
        for i in range(len(self.CHOICES)):        
            s               = random.choice(statements)        
            s               = s.replace("y",str(random.randint(0,100))).replace("z",str(random.randint(0,100)))
            X['choice'].append(s)
            s               = s.replace("!(","not(").replace("&&","and").replace("||","or")
            x               = X['lower']+1
            lower_condition = eval(s)
            x               = X['upper']-1
            upper_condition = eval(s)
            X['answer'].append(lower_condition and upper_condition)

        return X   


        
if __name__=="__main__":
    pass
    
