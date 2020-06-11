# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:01:56 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np



class model_31(MultipleChoice):
    
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
    
    QUESTION        = """The following code will display ______.
        
    public class main {{
    	public static void main(String[] args) {{
    		int list[] = {{ {list} }};
    		for (int i = {lower[0]}; i < list.length{type}; i++)
    			list[i] = list[i {sign} 1];
    		for (int i = {lower[1]}; i < list.length; i++)
    			System.out.print(list[i] + " ");
    	}}
    }}
        """
    shuffle = True
    def model(self):
        X               = {} 
        Type = ["list[i] = list[i + 1]", "list[i] = list[i - 1]"]        
        # creating list
        List        = random.sample(list(range(0,10)),k=7)
        X['list']   = str(List)[1:-1]
        X['lower']  = [ random.randint(1,len(List)-3),
                        random.randint(1,len(List)-3)]
        ######## question types
        if Type == "list[i] = list[i - 1]":
            X['type'] = ""
            X['sign'] = "-"
        else:
            X['type'] = "-1"
            X['sign'] = "+"             
        ### code ####
        output = List.copy()
        upperbound = len(List) if X['sign']=="-" else len(List)-1
        for i in range(X['lower'][0],upperbound):
            output[i] = output[i-1] if X['sign']=="-" else output[i+1]
        correct = output[X['lower'][1]:]
        #### wrong choices #####
        choices = []
        choices.append(List[X['lower'][0]:]) 
        choices.append(List[X['lower'][1]:]) 
        choices.append(output)
        choices.append(output[X['lower'][0]:])
        choices.append(List[1:] + List[0:1])
        choices.append((List[1:] + List[0:1])[X['lower'][1]:])

        wrong = [] 
        for i in choices:
            if i not in wrong: # removing repetitive choices if exists.
                wrong.append(i)
                
        if correct in wrong: 
            wrong.remove(correct) # removing correct from potential wrong choices
        X['answer'] = str(correct)[1:-1].replace(",","")
        X['choice'] = random.sample(choices,k=4)
        X['choice'].append(correct) 
        X['choice'] = [str(i)[1:-1].replace(",","") for i in X['choice']]
        random.shuffle(X['choice'])          

        return X  


        
if __name__=="__main__":
    pass
    
