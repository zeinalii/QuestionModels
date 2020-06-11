# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:58:06 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np



class model_19(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "true",
                            "false"]
    
    QUESTION        = """What is the value of the following expression?
            
            {expression}
            
        """
    shuffle = False
    def model(self):
        X               = {} 
          
        X['state']      = random.sample(["true","false","true","false"],k=3)
        
        X['o']          = random.sample(["||","&&"],k=2)
        X['expression'] = "{state[0]} {o[0]} {state[1]} {o[1]} {state[2]}".format(**X)
        # calculating the output
        command         = X['expression'].replace("true","True").replace("false","False")
        command         = command.replace("&&","&").replace("||","|")
        X['answer']     = eval(command)
        return X        
    


        
if __name__=="__main__":
    pass
    
