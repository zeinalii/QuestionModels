# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:51:51 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np




class model_5(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs = [
                'ASCII',
                ]   

    CHOICES    = [ "{choice[0]}",
                    "{choice[1]}",
                    "{choice[2]}",
                    "{choice[3]}"]
    QUESTION   = "Note that the ASCII value for character {character} is {ASCII}. \
What does the expression \'{character}\' {sing} 1 evaluate to?"

    def model(self):
        X       = {}
        if random.random() < 0.5:
            X['sing']       = '+'
            X['character']  = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXY')
            X['ASCII']      = ord(X['character'])
            X['choice']     = [ X['ASCII'] + 1,
                                chr(X['ASCII'] + 1),
                                X['character'] + '1',
                                "Syntax error (illegal expression)"]
            X['answer']     = X['ASCII'] + 1
        else:
            X['sing']       = '-'            
            X['character']  = random.choice('BCDEFGHIJKLMNOPQRSTUVWXYZ')
            X['ASCII']      = ord(X['character'])
            X['choice']     = [ X['ASCII'] -1 ,
                                chr(X['ASCII'] -1 ),
                                X['character'] + '-1',
                                "Syntax error (illegal expression)"]
            X['answer']     = X['ASCII'] -1            
        return X
    


        
if __name__=="__main__":
    pass
    
