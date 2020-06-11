# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:02:36 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np

class model_32(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "0",
                        "1",
                        "2",
                        "3",
                        "4",
                        "5"]

    QUESTION        = """The following code will display ______.
        
		double[] myList = {{ {list} }};
		double {type} = myList[0];
		int indexOf{type} = 0;
		for ({loop}) {{
			if (myList[i] > {type}) {{
				{type} = myList[i];
				indexOf{type} = i;
			}}
		}}
        System.out.println(indexOf{type});       
        """
    shuffle = True
    def model(self):
        X               = {} 
        ######## question types
        X['type'] = random.choice(["max", "min"])  
        direction = random.choice(["FromStart","FromEnd"])
        if direction == "FromStart":
            X['loop'] = "int i = 0; i < myList.length; i++"
        else:
            X['loop'] = "int i = myList.length-1; i >= 0; i--"
            

       # creating list
        List        = random.choices(list(range(0,10)),k=3)
        List        = List + List
        X['list']   = str(List)[1:-1]
        ### 
        if X['type'] == "min":
            temp = [i for i, j in enumerate(List) if j == min(List)]
            if direction == "FromStart":
                X['answer'] = min(temp)
            else:
                X['answer'] = max(temp)
        else:
            temp = [i for i, j in enumerate(List) if j == max(List)]
            if direction == "FromStart":
                X['answer'] = min(temp)
            else:
                X['answer'] = max(temp)            
          

        return X  




        
if __name__=="__main__":
    pass
    
