# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:39:43 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np


class model_1(MultipleChoice):
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs = [
                'substring',
                ]    
    QUESTION = """What is the return value of $$$"{string}".{method}{indeces}$$$?    """
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


        What is the return value of "CTmAbUotca".substring(4, 9)?
            .  bUotc
            .  Uotca
            .  bUotca
            .  mAbUotca

            Answer:  bUotc


            output is a list containing : [Question, Choices, Answer]
            """
        X               = {}
        X['method']     = "substring"  # method we want to use
        X['string']     = self.randomWord()  # generating a random un-repeated string with length of stringLength
        a               = random.randint(1, len(X['string']) - 1)  # lower bound   1<=a<=len(STRING)-1
        b               = random.randint(a, len(X['string']) - 1)  # upper bound a <=b<=len(STRING) -1
        X['indeces']    = (a, b)  # creating (a,b)
        #  choices
        if (X['string'][a:b] == ""):
            X['a'] = "an empty string"  # choice a is theCorrect answer
            X['b'] = "Syntax error (illegal expression)"  # choice b
        else:
            X['a'] = X['string'][a:b]  # choice a
            X['b'] = X['string'][a + 1:b + 1]  # choice b
        X['c'] = X['string'][a: b + 1]  # choice c
        if len(X['string']) == b + 1:
            X['d'] = X['string'][a - 2: b + 1]  # choice d
        else:
            if X['string'][a + 1:b + 2] == "":
                X['d'] = "an empty string"
            else:
                X['d'] = X['string'][a + 1:b + 2]
        X['answer'] = X['a']
        if len(set([X['a'], X['b'], X['c'], X['d']])) != 4:
            return self.model()
        else:
            return X

    def randomWord(self):
        return random.choice(self.WORDS['words'])   



        
if __name__=="__main__":
    pass
    
