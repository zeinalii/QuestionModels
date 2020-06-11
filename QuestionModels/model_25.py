# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:59:58 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np



class model_25(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}",
                            "{choice[4]}"]
    
    QUESTION        = """The following code will display ______.
        
    class test 
    {{
        public static void main(String args[])
        {{
            int var1 = {num[0]}; 
            int var2 = {num[1]};
            if ((var2 = {num[2]}) == var1)
                System.out.print(var2);
            else 
                System.out.print(++var2);
        }} 
    }}        
        """
    shuffle = True
    
    def model(self):
        X               = {} 
        X['choice']     = []        
        X['num']        = [ random.randint(-50,-5),
                            random.randint(-2,5),
                            random.randint(10,50)]
        # # # # # code # # # # #
        if X['num'][1] == X['num'][0]:
            X['answer'] = X['num'][1]
        else:
            X['answer'] = X['num'][2] + 1
        X['choice'].append(X['num'][0])
        X['choice'].append(X['num'][1])
        X['choice'].append(X['num'][2])
        X['choice'].append(X['num'][1] + 1)
        X['choice'].append(X['num'][2] + 1)          
        return X  


        
if __name__=="__main__":
    pass
    
