# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:59:15 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np


class model_23(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "Apple ",
                            "Banana ",
                            "Orange",
                            "Apple Banana ",
                            "Apple Orange",
                            "Banana Orange",
                            "Nothing will be printed"]
    
    QUESTION        = """The following code displays __________?
        
        int x = {x};
        
        if ({exp[0]})
          x *= -1;  
          System.out.print("Apple ");
        if ({exp[1]})
          System.out.print("Banana ");
        else
          System.out.print("Orange");
        """
    shuffle = False
    def model(self):
        X               = {} 
        statements      = ['x > y || x > z','x > y && x > z']
        statements     += ['not(x > y) || x < z','not(x > y) && x < z']
        statements     += ['x > y || not(x < z)','x < y && not(x < z)']
        statements     += ['not(x > y || x > z)','not(x > y && x > z)']
        
        X['x']          = random.randint(-10,10)
        [s1,s2]         = random.sample(statements,k=2)        
        s1              = s1.replace("y",str(random.randint(-15,15))).replace("z",str(random.randint(-15,15)))
        s2              = s2.replace("y",str(random.randint(-15,15))).replace("z",str(random.randint(-15,15)))
        X['exp']        = [s1, s2]
        # # # code execution # # # #
        x               = X['x']
        s1              = s1.replace("!(","not(").replace("&&","and").replace("||","or")
        s2              = s1.replace("!(","not(").replace("&&","and").replace("||","or")    
        # code
        output          = "Nothing will be printed"
        if eval(s1):    x *= -1;
        output          = "Apple "
        if eval(s2):    output += "Banana "
        else:           output += "Orange"       
        #
        # # # # # # # # # # # # # # #
        X['answer']     = output
          

        return X          



        
if __name__=="__main__":
    pass
    
