# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:58:24 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np



class model_20(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         =  [ "too hot too cold just right",
                            "just right",
                            "too cold",
                            "too hot"]
    
    QUESTION        = """The following code display __________.
            
            double temperature = {tem};
            
            if (temperature >= 100)
              System.out.println("too hot");
            else if (temperature <= 20)
              System.out.println("too cold");
            else
              System.out.println("just right");

        """
    shuffle = True
    def model(self):
        X               = {} 
          
        X['tem']        = random.randint(-30,250)
        
        # # # # code # # # #
        output          = "too hot too cold just right"
        if (X['tem'] >= 100):   output = "too hot"
        elif (X['tem'] <= 20):  output = "too cold"
        else:                   output = "just right"
        # # # # # # # # # #

        X['answer'] = output
        return X          


        
if __name__=="__main__":
    pass
    
