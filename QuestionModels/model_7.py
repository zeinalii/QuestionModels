# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:52:21 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np





class model_7(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs = [
                'DoubleToInteger',
                'decimal',
                ]   

    CHOICES    = [ "$$$( int )( {value[0]:7.4f} * {value[1]} ) / {value[1]}$$$",
                            "$$$( int )( {value[0]:7.4f} * {value[1]} ) / {value[1]}.0$$$",
                            "$$$( int )( {value[0]:7.4f} * {value[1]} / {value[1]} )$$$",
                            "$$$( int )( {value[0]:7.4f} ) * {value[1]} / {value[1]}.0$$$"]
    QUESTION   = "Which of the following expression results in {question}?"
    ANSWER     = "$$$( int )( {value[0]:7.4f} * {value[1]} ) / {value[1]}$$$"
    
      
            
    def model(self):
        X           = {}
        X['value']  = [random.random()*100,            # generating a random number between 0 and 100
                         random.choice([10,100,1000])] # choosing values between 10,100,1000
        
        X['question'] = int(X['value'][0]*X['value'][1])/X['value'][1]
        
        X['answer']     = self.CHOICES[0].format(**X)
        return X
    

        
if __name__=="__main__":
    pass
    
