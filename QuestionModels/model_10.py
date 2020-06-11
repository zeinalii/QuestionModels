# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:53:27 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np




class model_10(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs        = [
                        'boolean',
                        ]   

    CHOICES         = [ " banana",
                        " apple",
                        " apple orange",
                        " orange",
                        " apple banana",
                        " apple apple"]
    QUESTION        = """Suppose x = {x}, y = {y}, and z = {z}. What is the printout of the following statement? Hint: Indent the statement
correctly first.

String fruit = "unassigned";
if( x > 0 )
{{
    fruit = "apple";
if( y > 0 )
    System.out.print( " " + fruit );
else if( z > 0 )
    fruit = "orange";
    System.out.print( " " + fruit );

}}
else
    fruit = "banana";
    System.out.println( " " + fruit ); 
    """
    
            
    def model(self):
        X           = {}
        X['x']  = random.randint(-1,2)
        X['y']  = random.randint(-1,1)
        X['z']  = random.randint(-1,1)
        
        def temp(x,y,z):
            fruit = "unassigned"
            PrintString = ""
            if (x>0):
                fruit = "apple"
                if y> 0:
                    PrintString += " " + fruit
                elif z>0:
                    fruit = "orange"
                PrintString += " " + fruit
            else:
                fruit = "banana"
                PrintString += " " + fruit
            return PrintString
        
        X['answer'] = temp(X['x'],X['y'],X['z'])
        if X['answer'] not in self.CHOICES:
            self.CHOICES[4] = X['answer']            
        return X    
    


        
if __name__=="__main__":
    pass
    
