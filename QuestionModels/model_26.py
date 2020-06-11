# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:00:16 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np



class model_26(MultipleChoice):
    
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
        
    class test 
    {{
        public static void main(String args[])
        {{
             int sum = 0;
             for (int i = {lower[0]}, j = {lower[1]}; i < {upper[0]} & j < {upper[1]}; ++i, j = i + 1)
                 sum += i;
            tem.out.println(sum);
        }} 
    }}        
        """
    shuffle = True
    def model(self):
        X               = {} 
          
        X['choice']     = []
        
        X['lower']      = [ random.randint(0,3),
                            random.randint(0,3)]
        
        X['upper']      = [ random.randint(4,9),
                            random.randint(4,9)]
        #####
        choices         = [0,0]
        for i,j in zip(range(X['lower'][0],X['upper'][0]),range(X['lower'][1],X['upper'][1])):
            choices[0] += i
            choices[1] += j

        choices.extend([sum(range(X['lower'][0],X['upper'][0])),
                        sum(range(X['lower'][1],X['upper'][1])),
                        sum(range(X['lower'][0],X['upper'][0]+1)),
                        sum(range(X['lower'][1],X['upper'][1]+1))])
        X['answer']     = choices[0]
        if len(set(choices)) == 3:
                choices.append("compilation error")
        elif len(set(choices)) < 3:
            return self.model()
        
        X['choice'] = list(set(choices))

        return X          


        
if __name__=="__main__":
    pass
    
