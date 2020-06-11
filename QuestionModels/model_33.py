# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:02:53 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np


class model_33(MultipleChoice):
    
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
    
    QUESTION        = "Which of the following is correct? "
    shuffle = True
    def model(self):
        Type            = ["double", 
                                 "float",
                                 "int",
                                 "long",
                                 "short",
                                 "char",
                                 "boolean"]
        c           = {}
        correct     = [ "{type}[] a = new {type}[{num}];"]
        wrong       = [ "{type}[] a = new {type}({num});",
                        "{type}[] a = new {type}{{{num}}};",
                        "{type}[] a = {type}({num});",
                        "{type}[] a = {type}{{{num}}};",
                        "{type}[] a = new ({num});",
                        "{type}[] a = new {{{num}}};",
                        "{type} a = new {type}({num});",
                        "{type} a = new {type}{{{num}}};",
                        "{type} a = {type}({num});",
                        "{type} a = {type}{{{num}}};",
                        "{type} a = new ({num});",
                        "{type} a = new {{{num}}};",
                        "{type}() a = new {type}({num});",
                        "{type}() a = new {type}{{{num}}};",
                        "{type}() a = {type}({num});",
                        "{type}() a = {type}{{{num}}};",
                        "{type}() a = new ({num});",
                        "{type}() a = new {{{num}}};",
                        "{type} a[] = new {type}({num});",
                        "{type} a[] = new {type}{{{num}}};",
                        "{type} a[] = {type}({num});",
                        "{type} a[] = {type}{{{num}}};",
                        "{type} a[] = new ({num});",
                        "{type} a[] = new {{{num}}};",
                        "{type}[] = new {type}[{num}];",
                        "{type}[] = new {type}({num});",
                        "{type}[] = new {type}{{{num}}};",
                        "{type}[] = {type}({num});"]
        X           = {} 
        c['type']   = random.choice(Type)
        c['num']    = random.randint(2,20)
        X['answer'] = correct[0].format(**c)
        choices     = correct + random.sample(wrong,k=4)
        X['choice'] = []
        for i in choices:
            c['type']   = random.choice(Type)
            c['num']    = random.randint(2,20)            
            X['choice'].append(i.format(**c))
                      

        return X  



        
if __name__=="__main__":
    pass
    
