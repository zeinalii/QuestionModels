import random
import sympy as sym
from sympy.parsing.sympy_parser import (parse_expr)
import re

class ShortAnswer:
    QUESTION    = ""
    CODE        = ""
    EQ          = ""
    def __init__(self):
        self.EQ = self.generateEq()
    
    def __str__(self):
        pass

    def generate(self):
        pass
        



    def generateSimpleEq(self,variable_str = ['x','y'],complexity=0):
        variables = [sym.Symbol(i) for i in variable_str]
        if complexity == 0:
            eq = sym.Symbol('eq')
            for i,var in enumerate(variables):
                if i==0:
                    eq = random.randint(1,9)*var
                else:
                    eq += random.randint(-9,9)*var
            return eq   
        elif complexity == 1:
            eq = sym.Symbol('eq')
            for i,var in enumerate(variables):
                if i==0:
                    eq = random.randint(1,9)*(var**random.randint(1,5))
                else:
                    eq += random.randint(-9,9)*(var**random.randint(1,5))
            return eq   
        elif complexity == 2:
            eq = sym.Symbol('eq')
            for i,var in enumerate(variables):
                if i==0:
                    eq = random.randint(1,9)*(var**random.randint(1,3))*(random.choice(variables)**(random.randint(1,3)))
                else:
                    eq += random.randint(-9,9)*(var**random.randint(1,5))*(random.choice(variables)**(random.randint(1,3)))
            return eq   
        elif complexity == 3:
            eq = sym.Symbol('eq')
            for i,var in enumerate(variables):
                if i==0:
                    eq = random.randint(1,9)*(var**random.randint(1,3))*(random.choice(variables)**(random.randint(1,3)))
                else:
                    eq += random.randint(-9,9)*(var**random.randint(1,5))*(random.choice(variables)**(random.randint(1,3)))
            return eq   
        elif complexity == 4:
            eq = sym.Symbol('eq')
            for i,var in enumerate(variables):
                if i==0:
                    eq = random.randint(1,9)*(var**random.randint(1,3))*(random.choice(variables)**(random.randint(1,3)))
                else:
                    eq += random.randint(-9,9)*(var**random.randint(1,5))*(random.choice(variables)**(random.randint(1,3)))
            if random.random() > 0.5:
                return random.choice([-1,1]) * sym.sqrt(eq)
            else:
                return random.choice([-1,1]) * eq ** random.randint(2,5)   



    def generateIntegerEq(self):
        var = sym.Symbol("C")
        num = (random.randint(1,99),random.randint(1,99))
        return var * sym.simplify("%d/%d"%num)
  
    
    
    def generateEq(self):
        return ((self.generateSimpleEq(['x','y'],complexity=4)) + \
                self.generateIntegerEq())/\
                self.generateSimpleEq(['x','y'],complexity=0)
    

if __name__=="__main__":
    s = []
    for i in range(100):
        shoranswer = ShortAnswer()
        eq = shoranswer.generateEq()
        if (len(eq.args)) > 2:
            s.append(eq)
            


# -*- coding: utf-8 -*-
"""
Created on Wed May  6 02:30:20 2020
@author: AmirHossein
"""
import sympy as sym
import re
shoranswer = ShortAnswer()
eq = shoranswer.generateEq()



eq_java     = '( 2*C/34*5 + Math.pow((8*Math.pow(x,6) + 2*x*Math.pow(y,3)),4))/(9*x - 7*y)'
eq_python   = '(2*C/34*5 + (8*x**6 + 2*x*y**3)**4)/(9*x - 7*y)'


def calculateGrade(eq_python,eq_java):
    grade = {
            'numerator'     :0,
            'denominator'   :0,
            'syntax'        :0,
            'overall'       :0
            }
    javaCode = """class Test {  
                    int C = 11;
                    double x =2,y=3;
                    double java = %s;}"""%eq_java


    numerator_eq_python     = fixBracket(re.search(r'\((.*)\)\s*/\s*\((.*)\)\s*',eq_python).group(1))
    denominator_eq_python   = fixBracket(re.search(r'\((.*)\)\s*/\s*\((.*)\)\s*',eq_python).group(2))    
    numerator_eq_java       = fixBracket(re.search(r'\((.*)\)\s*/\s*\((.*)\)\s*',eq_java).group(1))
    denominator_eq_java     = fixBracket(re.search(r'\((.*)\)\s*/\s*\((.*)\)\s*',eq_java).group(2))

    if isEqual(numerator_eq_python,numerator_eq_java):
        grade['numerator'] = 1
    if isEqual(denominator_eq_python,denominator_eq_java):
        grade['denominator'] = 1
    if isEqual(eq_python,eq_java) and is_syntax_correct(javaCode):
        grade['syntax'] = 1
    grade['overall'] = grade['numerator'] + grade['denominator'] + grade['syntax']

    return grade
        
        
def is_syntax_correct(javaCode):
    from javalang.parse import parse
    try:
        parse(javaCode)
        return True
    except:
        return False        
        


def isEqual(python,java):
    isSame  = True 
    eq_python   = parse_expr(python)
    eq_java     = parse_expr(convert(java))
    if sym.simplify(eq_python - eq_java) != 0 or eq_python.compare(eq_java) !=0:
        isSame = False
    return isSame    
 


def fixBracket(s):
    op = 0
    cl = 0
    for i in s:
        if i == '(':
            op += 1
        if i == ')':
            cl += 1   
    if op > cl:
        return s + ')'*(op-cl)
    if cl > op:
        return '('*(cl-op) + s
    else:
        return s


def convert(code):
    # type conversion
    code = re.sub(r'\(\s*double\s*\)\s*(\w+\.{0,1}\w*)', r"N(\1)", code)
    code = re.sub(r'\(\s*double\s*\)\s*\(', r"N(", code)
    code = re.sub(r'\(\s*int\s*\)\s*(\w+\.{0,1}\w*)', r"Integer(\1)", code)
    code = re.sub(r'\(\s*int\s*\)\s*\(', r"Integer(", code)    
    code = re.sub(r'\(\s*long\s*\)\s*(\w+\.{0,1}\w*)', r"Integer(\1)", code)
    code = re.sub(r'\(\s*long\s*\)\s*\(', r"Integer(", code)  
    code = re.sub(r'\(\s*short\s*\)\s*(\w+\.{0,1}\w*)', r"Integer(\1)", code)
    code = re.sub(r'\(\s*short\s*\)\s*\(', r"Integer(", code)       
    # java method conversion to python
    code = code.replace("Math.","").replace("pow","Pow").replace("  "," ")
    return code


















s = '5* (double) C/34 + (8*x**6 + 2*x*y**3)**4'
Braket_is_Balanced(s)
# Function to check parentheses 
def Braket_is_Balanced(myStr): 
    open_list = ["("] 
    close_list = [")"] 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return False
    if len(stack) == 0: 
        return True
    else: 
        return False
  





















