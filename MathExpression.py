# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 05:15:10 2020

@author: AmirHossein
"""



# Short Answer
""" The answer should be a string with a maximum length of 25 characters"""

import random

class MathExpression:
    def __init__(self):
        self.CHOICES    = [ "{a:2.2f}",
                            "{b:2.2f}",
                            "{c:2.2f}",
                            "{d:2.2f}",
                            "{e:2.2f}"]

    def GenerateQuestion(self,X):
        """replace X inside the Qestion and Choices and then print them """
        print('\n')
        print(self.QUESTION.format(**X))
        for i in self.CHOICES: 
            print(". ",i.format(**X))
        print("\nAnswer: ", self.CHOICES[0].format(**X))
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.CHOICES[0].format(**X)]
    

    def generate(self):
        self.QUESTION = "The expression {x1} + {x2} / ({x3} - {x4}) * {x5} is evaluated to"
        X = {}
        X['x1'] = random.randint(1,5)
        X['x2'] = random.choice([6,12,18,24])
        X['x3'] = random.randint(1,2)
        X['x4'] = X['x3'] + 2
        X['x5'] = random.randint(1,3)
        
        X['a'] = X['x1']    +   X['x2'] / (X['x3'] - X['x4']) * X['x5']
        X['b'] = X['x1']    +   X['x2'] / ( (X['x3'] - X['x4']) * X['x5']   )
        X['c'] = (X['x1']   +   X['x2'])    / (X['x3'] - X['x4'])   *   X['x5']
        X['d'] = (X['x1']   +   X['x2'])    /  (   (X['x3'] - X['x4']) * X['x5']   )
        X['e'] = X['x1']    +   X['x2'] / ( X['x3'] + X['x4']) * X['x5']
        
        if (X['a'] == X['b'] or 
            X['a'] == X['c'] or
            X['a'] == X['d'] or
            X['a'] == X['e'] or
            X['b'] == X['c'] or
            X['b'] == X['d'] or
            X['b'] == X['e'] or
            X['c'] == X['d'] or
            X['c'] == X['e'] or
            X['d'] == X['e']):
            return self.generate()
        return self.GenerateQuestion(X)


        
if __name__ == "__main__":
    
    mathexpression = MathExpression()
    _ = mathexpression.generate()


     