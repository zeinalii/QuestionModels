# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:52:05 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np




class model_6(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs = [
                'Final',
                'constant',
                ]   

    CHOICES    = [ "$$$final double {variable} = {value:2.2f}$$$",
                               "$$$final {variable} = {value:2.2f}$$$",
                               "$$$final long {variable} = {value:2.2f}$$$",
                               "$$$double {variable} = {value:7.2f}$$$"]
    QUESTION   = """To declare a constant {variable} inside a method with value {value:2.2f}, you write:"""
    shuffle = False
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        DIR     = os.path.join(BASE_DIR,'data','javanameconvention.json')
        with open(DIR) as f:
            self.name = json.load(f)
            
            
    def model(self):
        X               = {}
        X['value']      = random.random()*100
        X['variable']   = random.choice(self.name['adjective']).upper() +\
                            "_" + random.choice(self.name['descriptiveName']).upper()
        X['answer']     = self.CHOICES[0].format(**X)
        return X
        


        
if __name__=="__main__":
    pass
    
