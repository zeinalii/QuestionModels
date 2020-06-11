# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:56:52 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np




class model_17(MultipleChoice):
    
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
    
    QUESTION        = """What will be the output of the following Java code?
        class operators
        {{
            public static void main(String args[])
            {{
                int var1 = {num[0]};
                int var2 = {num[1]};
                int var3;
                var3 = {expression};
            }}
        }}
        
        """
    shuffle = True
    def model(self):
        X               = {} 
        X['op']         = [random.choice(['++','--']),
                             random.choice(['+','-','*']),
                             random.choice(['+','-','*']),
                             random.choice(['++','--'])]
        
        X['num']        = [random.randint(2,10), random.randint(2,10)]
        X['expression'] = "{op[0]} var1 {op[1]} var2 {op[2]} var1 {op[3]}".format(**X)
        a               = X['num'][0]+1 if X['op'][0]=="++" else X['num'][0]-1
        a_1             = X['num'][0]-1 if X['op'][0]=="++" else X['num'][0]+1
        b               = X['num'][1]
        c               = a
        c_1             = a if X['op'][3]=="++" else a-1
        c_2             = X['num'][0]+1 if X['op'][3]=="++" else X['num'][0]-1
        
        X['answer']     = eval("%d %s %d %s %d"%(a,X['op'][1],b,X['op'][2],c)) 
        # wrong choices
        choices         = [eval("%d %s %d %s %d"%(a,X['op'][1],b,X['op'][2],c)),
                           eval("%d %s %d %s %d"%(a_1,X['op'][1],b,X['op'][2],c)),
                           eval("%d %s %d %s %d"%(a,X['op'][1],b,X['op'][2],c_1)),
                           eval("%d %s %d %s %d"%(a_1,X['op'][1],b,X['op'][2],c_1)),
                           eval("%d %s %d %s %d"%(a,X['op'][1],b,X['op'][2],c_2)),
                           eval("%d %s %d %s %d"%(a,X['op'][1],b,X['op'][2],c_2)) ,
                           eval("%d %s %d %s %d"%(a,X['op'][1],b,X['op'][2],c))+1,
                           eval("%d %s %d %s %d"%(a,X['op'][1],b,X['op'][2],c))-1,
                           eval("%d %s %d %s %d"%(a,X['op'][1],b,X['op'][2],c))-2,
                           eval("%d %s %d %s %d"%(a,X['op'][1],b,X['op'][2],c))+2
                           ]
        choices = list(set(choices))
        # creating final choices and adding the correct answer
        if len(choices)>4:
            X['choice'] = random.sample(choices,k=5)
            if X['answer'] not in X['choice']:
                X['choice'][-1] = X['answer']
        else:
            return self.model()
            
        return X   


        
if __name__=="__main__":
    pass
    
