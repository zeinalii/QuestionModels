# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:02:52 2020

@author: AmirHossein
"""



import random
import os
import json

class ShortAnswerQuestion:
    def __init__(self):

        self.ANSWER     = "{answer}"
        self.BASE_DIR    = os.path.dirname(os.path.dirname(__file__))

        
    def generate(self):
        for i in range(1,2):
            [QUESTION, CHOICES, ANSWER] = eval("self.model_%d()"%i)
            
            print('\n Question %d'%i)
            print(QUESTION)
            print("\n\nanswer: ", ANSWER)
          

    def model_1(self):
        self.QUESTION   = """The following code will display ______.
        
     int arr[] = new int[{num}];
     for (int i = {lower}; i < arr.length; i++)
            arr[i] = i * {C}
		System.out.println(arr[]);
        """

        X               = {}
        X['num']        = random.randint(1,6)
        X['C']          = random.randint(1,6)
        X['lower']      = random.randint(0,X['num'])
        code            = ["","""
        for (int i = {lower}; i < arr.length; i++)
            arr[i] = i * {C}
        """]
        
        
        return [self.QUESTION.format(**X),
                self.ANSWER.format(**X)]




if __name__ == "__main__":
    
    question    = ShortAnswerQuestion()
    _           = question.generate()