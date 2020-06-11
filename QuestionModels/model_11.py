# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:53:52 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np




class model_11(NamingConvention):
    
    TYPE = "multiplechoice_MultiAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs        = [
                        'NamingConvention',
                        ]   

    CHOICES         = ["a. class name",
                       "b. method name",
                       "c. variable name",
                       "d. none"
                       ]
    
    QUESTION        = """In the following peice of code, which identifier's name is \
        chosen incorect based on the java naming convention. Select all that apply.
        
public class {class[0]} {{
        public double void {method[0]} (double x) {{
                return (x*x + 1);
                }}
       public static void main(String[] args) {{
       double {variable[0]};
       System.out.println({method[0]}());
       }}
}}
        """
    shuffle = False
            
    def model(self):
        X                = {} 
        X['method']      = self.generateMethod()
        X['variable']    = self.generateVariable()
        X['class']       = self.generateClass()
        ANSWER           = [X[i][1] for i in X]
        if True not in ANSWER: ANSWER.append(True)  
        else : ANSWER.append(False)
        X['answer']     = ANSWER
        return X    
    



        
if __name__=="__main__":
    pass
    
