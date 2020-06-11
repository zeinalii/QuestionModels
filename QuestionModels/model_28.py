# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:01:03 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np



class model_28(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
    
    QUESTION        = """The following code will display ______.
        
        for (int i = {start}; i < {end}; i++)
            if (i % {divisor} == {remainder})
                System.out.print(i + " ");
        """
    shuffle = True
    
    
    def model(self):
        X               = {} 
        X['start']      = random.randint(0,5)
        X['end']        = random.randint(12,21)
        X['divisor']    = random.randint(2,6)
        X['remainder']  = random.randint(0,X['divisor']-1)
        def fun(s,e,d,r):
            t = ""
            for i in range(s,e):
                if (i%d) == r:
                    t += "%d "%i
            return t
        
        choices         = []
        choices.append(fun(X['start'],X['end'],X['divisor'],X['remainder']))                #(p+q)*q + r
        choices.append(fun(X['start'],X['end']+X['divisor'],X['divisor'],X['remainder']))   #(p-q)*q + r
        choices.append(fun(X['start'],X['end']-X['divisor'],X['divisor'],X['remainder']))   
        choices.append(fun(X['start'],X['end'],X['divisor'],X['remainder']-1))
        choices.append(fun(X['start'],X['end'],X['divisor'],X['remainder']+1))
        choices.append(fun(X['start'],X['end'],X['divisor']+1,X['remainder']+1))
        choices.append(fun(X['start'],X['end'],X['divisor']-1,X['remainder']+1))
        
        X['answer']     = choices[0]
        if len(set(choices)) < 5 or choices[0]=='':
            return self.model()
        else:
            choices = list(set(choices))
            
        if '' in choices:
            choices.remove('')
        X['choice']     = random.sample(choices,4)
        if X['answer'] not in X['choice']:
            X['choice'][-1] = X['answer']
        
          

        return X  


        
if __name__=="__main__":
    pass
    
