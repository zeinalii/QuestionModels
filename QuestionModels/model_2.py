# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:49:31 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np



class model_2(MultipleChoice):
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs = [
                'indexOf',
                ]    
    QUESTION = """What is the return value of $$$"{string}".{method}{indeces}$$$?"""
    CHOICES    = ["{a}",
                  "{b}",
                  "{c}",
                  "{d}"]
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        DIR     = os.path.join(self.BASE_DIR,'data','words.json')
        with open(DIR) as f:
            self.WORDS = json.load(f)
            
    def model(self):
        """ Generate random multiple choice questions
        
        for example:
        What is the return value of "JTKqE".indexOf('qE', 0)?
        .  3
        .  2
        .  4
        .  5
        
        Answer:  3     
        """
        X           = {}
        X['method'] = "indexOf"                                            # method we want to use
        X['string'] = self.randomWord()                                    # generating a random un-repeated string with length of stringLength
        i           = random.randint(0,len(X['string'])-1)                 # lower bound   1<=a<=len(STRING)-1
        if random.random() < 0.8:                                          #the character is inside the string
            a           = X['string'][i]
            X['indeces']= "('{}')".format(a) 
            X['a']      = X['string'].index(a)
            X['b']      = X['a'] - 1
            X['c']      = X['a'] + 1
            X['d']      = X['a'] + 2
                                                     
        else: 
            a           = X['string'][i].lower() if X['string'][i].isupper() else X['string'][i].upper()
            X['indeces']= "('{}')".format(a) 
            X['a']      = -1
            X['b']      = "false" 
            X['c']      = i
            if X['c'] == len(X['string']):
                X['d']  = i - 1
            else:
                X['d']  = i + 1      
        X['answer'] = X['a']
        if len(set([X['a'],X['b'],X['c'],X['d']])) != 4: 
            return self.model()
        else:
            return X

    def randomWord(self):
        return random.choice(self.WORDS['words'])   



        
if __name__=="__main__":
    pass
    
