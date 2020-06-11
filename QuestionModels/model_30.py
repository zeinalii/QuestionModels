# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:01:36 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np


class model_30(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}",
                            "{choice[4]}",
                            "{choice[5]}"]
    
    QUESTION        = """The following code will display ______.
        
    int arr[] = new int[{num}];
    {code}
    System.out.println(arr{index});
        """
    shuffle = True
    def model(self):
        X               = {} 
        X['num']        = random.randint(2,6)
        X['C']          = random.randint(2,6)
        X['lower']      = random.randint(0,X['num']-1)
        index           = random.randint(0,X['num']-1)
        code            = ["","""    for (int i = {lower}; i < arr.length; i++)
        arr[i] = i * {C};""".format(**X)]
        code = random.choice(code)
        if code != "":
            ################ code #################
            arr = np.zeros(X['num'])
            _arr = np.zeros(X['num']) #for wrong choice
            for i in range(len(arr)):
                if i>=X['lower']:
                    arr[i]  = i * X['C']
                _arr[i] = i
            #######################################
            answer          = str(int(arr[index]))
            choices         = [str(int(arr[index]))]
            choices.append(str(int(_arr[index])))
            choices.append(str([int(i) for i in arr]))
            choices.append(str([int(i) for i in _arr[X['lower']+1:]]))
            choices.append(str([int(i) for i in _arr]))
            choices.append("class name @ hashcode")
        else:
            answer          = "0"
            choices         = ["0"]
            choices.append(str(["0"]*X['num']))
            choices.append("0"*X['num'])
            choices.append("run-time error")
            choices.append("complier error")
            choices.append("class name @ hashcode")
            answer
        X['index']  = random.choice(["",index]) 
        if X['index']=="":
            answer = choices[-1]
        X['choice'] = choices   
        X['code']   = code
        X['answer'] = answer
        if len(set(X['choice'] )) < 6:
            return self.model()
          

        return X   



        
if __name__=="__main__":
    pass
    
