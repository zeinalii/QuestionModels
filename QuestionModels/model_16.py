# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:56:28 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np



class model_16(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        'precedence',
                        ]   

    CHOICES         = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}",
                            "{choice[4]}",
                            "{choice[5]}"] 
    
    QUESTION        = """What is the order of precedence (highest to lowest) of the following operators?
        1. {operator[0]}
        2. {operator[1]}
        3. {operator[2]}
        """
    shuffle = True
    def model(self):
        X               = {}        
        operators       = {
                        "10":["()"],
                        "9":["++","--","!"],
                        "8":["*","/","%"],
                        "7":["+","-"],
                        "6":[">","<","<=",">="],
                        "5":["==","!="],
                        "4":["&&"],
                        "3":["||"],
                        "2":["?:"],
                        "1":["=","+=","-=","/=","*=","%="]
                    }
        index           = random.sample(list(operators.keys()), k=3)
        X['choice']     = []
        X["operator"]   = [random.choice(operators[i]) for i in index]
        for i in index:
            for j in [k for k in index if k !=i]:
                k = [k for k in index if k !=i and k !=j][0]
                X['choice'].append("%d > %d > %d"%(index.index(i)+1,index.index(j)+1,index.index(k)+1))
                if int(i) > int(j) > int(k):
                    X['answer'] = X['choice'][-1]
        return X          


        
if __name__=="__main__":
    pass
    
