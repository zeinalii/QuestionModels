# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:51:08 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np




class model_3(MultipleChoice):
    
    QUESTION   = "The expression $$${expression}$$$ is evaluated to"
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs = [
                'MathExpression',
                ]   
    CHOICES    = [ "{choice[0]}",
                    "{choice[1]}",
                    "{choice[2]}",
                    "{choice[3]}",
                    "{choice[4]}"]    
    
    
    def model(self):
        X = {}
        X['x'] = random.sample([i for i in range(1,21)],4)
        random.shuffle(X['x'])
        X['o'] = random.sample(['//','-','*'],k=3)
        X['o'].append(random.choice(['+','//','-','*']))
        bracket = "({x[2]} {o[3]} {x[3]})".format(**X)
        X['x'][3] = bracket
        random.shuffle( X['x'])
        expression = "{x[0]} {o[0]} {x[1]} {o[1]} {x[2]} {o[2]} {x[3]}".format(**X)
        try:
            X['expression'] = expression.replace('//','/')
            X['answer'] = eval(expression)
            choice = [expression]
            choice.append("({x[0]} {o[0]} ({x[1]} {o[1]} {x[2]})) {o[2]} {x[3]}".format(**X))
            choice.append("(({x[0]} {o[0]} {x[1]}) {o[1]} {x[2]}) {o[2]} {x[3]}".format(**X))
            choice.append("{x[0]} {o[0]} (({x[1]} {o[1]} {x[2]}) {o[2]} {x[3]})".format(**X))
            choice.append("{x[0]} {o[0]} ({x[1]} {o[1]} ({x[2]} {o[2]} {x[3]}))".format(**X))
            choice.append("(({x[0]} {o[0]} {x[1]}) {o[1]} ({x[2]} {o[2]} {x[3]}))".format(**X))
            for i in range(6):
                choice.append('int(' + choice[i].replace('//','/') + ')')
            choice = [eval(i) for i in choice]
            if len(set(choice)) > 4:
                X['choice'] = random.sample(set(choice),5)
                if X['answer'] not in X['choice']:
                    X['choice'][0] = X['answer']
            else:
                return self.model()
        except:
             return self.model()
        return X


        
if __name__=="__main__":
    pass
    
