# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:57:43 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np



class model_18(MultipleChoice):
    
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
    
    QUESTION        = """Suppose x = {num[0]}, y = {num[1]}, and z = {num[2]}. What is the printout of the following statement? (Please indent the statement correctly first.)
            
            if ({num[0]} > {num[3]})
               if ({num[1]} > {num[4]})
                  System.out.print("output1 ");
            else if ({num[2]} > {num[5]})
                  System.out.print("output2 ");
                  System.out.println("output3");

        """
    shuffle = False
    def model(self):
        X               = {} 
        X['num']        = [  random.randint(-10,10),
                             random.randint(-10,10),
                             random.randint(-10,10),
                             random.randint(-10,10),
                             random.randint(-10,10),
                             random.randint(-10,10)]
        
        # # # # code # # # #
        output          = ""
        if (X['num'][0] > X['num'][3]):
           if (X['num'][1] > X['num'][4]):
               output += "output1 "
           elif (X['num'][2] > X['num'][5]):
               output += "output2 "
        output += "output3"        
        # # # # # # # # # #
        X['choice']      = ["output1 ",
                                "output2 ",
                                "output3 ",
                                "output1 output3 ",
                                "output2 output3 "]
        X['answer'] = output          

        return X      


        
if __name__=="__main__":
    pass
    
