# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:01:20 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np


class model_29(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "int",
                            "double",
                            "boolean",
                            "char",
                            "void"]
    
    QUESTION        = """In the following code, you should fill in the blank with which return type?
        

    public class Test {{
    	public static void main(String[] args) {{
    		printGrade({num:2.2f});
    	}}
    
    	public static ________  getGrade(double score) {{
    		if (score >= 90.0)
    			{return[0]};
    		else if (score >= 80.0)
    			{return[1]};
    		else if (score >= 70.0)
    			{return[2]};
    		else if (score >= 60.0)
    			{return[3]};
    		else
    			{return[4]};
    	}}
    }}

        """
    shuffle = True
    def model(self):
        X               = {} 
        X['num'] = random.random()*100
        answer = random.choice(['int','double','boolean','char','void'])
        if answer =='void':
            X['return'] = [ "System.out.println('A')",
                            "System.out.println('B')",
                            "System.out.println('C')",
                            "System.out.println('D')",
                            "System.out.println('F')"]
        elif answer =='char':
            X['return'] = [ "return 'A'",
                            "return 'B'",
                            "return 'C'",
                            "return 'D'",
                            "return 'F'"]
        elif answer =='boolean':
            X['return'] = [ "return true",
                            "return true",
                            "return true",
                            "return true",
                            "return false"]             
                            
        elif answer =='int':
            X['return'] = [ "return 1",
                            "return 1",
                            "return 1",
                            "return 1",
                            "return 0"] 
            
        elif answer =='double':
            out         = {'x':[90,80,70,60,50]}
            X['return'] = [ "return {x[0]:2.1f}".format(**out),
                            "return {x[1]:2.1f}".format(**out),
                            "return {x[2]:2.1f}".format(**out),
                            "return {x[3]:2.1f}".format(**out),
                            "return {x[4]:2.1f}".format(**out)] 
        X['answer']     = answer            

        return X          



        
if __name__=="__main__":
    pass
    
