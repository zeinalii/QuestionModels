# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:56:08 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np



class model_15(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        'value Stored in variable',
                        ]   

    CHOICES         = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
    
    QUESTION        = """What is the value stored in x in the followin lines of Java code?
        int x, y, z;
        x = {num[0]};
        y = {num[1]}
        x = y = z = {num[2]}
        """
    shuffle = True
    def model(self):
        
        X               = {} 
        X['num']        = [ random.randint(-50,50),
                             random.randint(-50,50),
                             random.randint(-50,50)]
        X['answer']     = X['num'][2]
        X['choice']     = X['num']
        X['choice'].append("Syntax error (illegal expression)")
          

        return X      


        
if __name__=="__main__":
    pass
    
