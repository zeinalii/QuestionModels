# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:55:25 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np




class model_13(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        'average',
                        ]   
    QUESTION   = """If you enter {num[0]} {num[1]}, 
        when you run this program, what will be the output?
                
        
            import java.util.Scanner;
            
            public class Test1 {{
              public static void main(String[] args) {{
                Scanner input = new Scanner(System.in);
                System.out.print("Enter three numbers: ");
                int num1 = input.nextDouble();
                int num2 = input.nextDouble();
            
                // Compute average
                double average = {expression};
            
                // Display result
                System.out.println(average);
              }}
            }}        
        """
    CHOICES    = [ "{choice[0]}",
                    "{choice[1]}",
                    "{choice[2]}",
                    "{choice[3]}"] 
    def model(self):
       
        X               = {}
        expression      = []
        a        = int(random.random() * 100) / 10
        b        = int(random.random() * 100) / 10
        X['num'] = [a , b]
        expression.append('(int) (num1 + num2) / 2')
        expression.append('((int) num1 + num2)/2')
        expression.append('((int) num1 + (int) num2)/2')
        expression.append('(num1 + num2) / 2')
        choices = [float(int(a + b) / 2),
                   float((int(a)+b)/2),
                   float((int(a)+int(b))//2),
                   float((a+b)/2)]
        # choosing an expression from one the 4 availble options
        i = random.randint(0,3)
        X['expression'] = expression[i]
        X['answer']     = choices[i]
        # adding one more option if there wasn't 4 unique options
        if len(set(choices)) == 4:
            X['choice'] = choices
        elif len(set(choices)) == 3:
            X['choice'] = list(set(choices))
            X['choice'].append(int(X['answer']))
        else:
            return self.model()
        return X    
     


        
if __name__=="__main__":
    pass
    
