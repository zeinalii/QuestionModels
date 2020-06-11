# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:00:45 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np



class model_27(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
        
    
    QUESTION        = """Suppose int i = {i}, which of the following 
can be used as an index for array double[] t = new double[{index}]? select all that apply."""

    shuffle = False
    def model(self):
        X               = {} 
        X['index']  = random.randint(11,250)
        X['i']      = random.randint(0,X['index']) 
        
        choices     = []
        choices.append(["i",True if X['i'] in range(X['index']) else False])
        choices.append(["i*2",True if X['i']*2 in range(X['index']) else False])
        t = float(random.random()*100)
        choices.append(["(int) (i + %2.2f)"%t,True if X['i'] + t in range(X['index']) else False])
        t = random.randint(1,100)       
        choices.append(["i+%d"%t,True if X['i']+t in range(X['index']) else False])
        choices.append(["Math.random() * 10",False])
        choices.append(["(int) Math.random() * 10", True]) 
        choices.append(["(int) Math.random() * -10", True]) 
        choices.append(["(int) (Math.random() * 10)", True]) 
        choices.append(["(int) (Math.random() * -10)", False]) 
        choices.append(["(int) (Math.random() * 10)", True]) 
        choices.append(["(int) (Math.random() * -10)", False]) 
        
        temp        = random.sample(choices, k=5)
        X['choice'] = [i[0] for i in temp]
        X['answer'] = [i[1] for i in temp]
        return X   



        
if __name__=="__main__":
    pass
    
