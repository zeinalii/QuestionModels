# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:55:45 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np




class model_14(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        'precedence',
                        'operator',
                        ]   

    CHOICES         = [ "{choice[0]}",
                    "{choice[1]}",
                    "{choice[2]}",
                    "{choice[3]}"]
    
    QUESTION        = "Which of the following have {condition} precedence?"
    shuffle = True
    def model(self):
        highest = True if random.random() > 0.5 else False
        X               = {}        
        operators = {
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
        if highest:
            X['condition']  = "highest"
            index_correct   = random.randint(2,len(operators))
            index_wrong     = list(range(1,index_correct))
            X['answer']     = random.choice(operators[str(index_correct)])
        else:
            X['condition']  = "lowest"
            index_correct   = random.randint(1,len(operators)-2)
            index_wrong     = list(range(index_correct+1,len(operators)+1))
            X['answer']     = random.choice(operators[str(index_correct)])
            
        temp = []
        for i in index_wrong:
            for j in operators[str(i)]:
                temp.append(j)
        X['choice'] =[X['answer']]
        X['choice'].extend(random.sample(temp,k=3))              

        return X    


        
if __name__=="__main__":
    pass
    
