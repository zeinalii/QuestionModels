



import random
import os
import json
import numpy as np


class VariableType:
    def __init__(self):
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
        self.ANSWER     = "{answer}"
        self.BASE_DIR    = os.path.dirname(os.path.dirname(__file__))

        
    def generate(self):
        for i in range(19,22):
            [QUESTION, CHOICES, ANSWER] = eval("self.model_%d()"%i)
            
            print('\n Question %d'%i)
            print(QUESTION)
            for choice in CHOICES: 
                print(". ",choice)
            print("\nanswer: ", ANSWER)
          


    def model_1(self):
        self.QUESTION   = """If you enter {num[0]} {num[1]}, 
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
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]        
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
            return self.model_01()
        
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]
        
        
    def model_2(self):
        self.QUESTION   = "Which of the following have {condition} precedence?"
        self.CHOICES    = [ "{choice[0]}",
                    "{choice[1]}",
                    "{choice[2]}",
                    "{choice[3]}"]
        highest = True if random.random() > 0.5 else False
        X               = {}        
        operators = {
                        "10":["()"],
                        "9":["++","--","!"],
                        "8":["*","/","%"],
                        "7":["+","-"],
                        "6":[">","<","<=",">="],
                        "5":["==","!="],
                        "4":["&&"],
                        "3":["||"],
                        "2":["?:"],
                        "1":["=","+=","-=","/=","*=","%="]
                    }
        if highest:
            X['condition']  = "highest"
            index_correct   = random.randint(2,len(operators))
            index_wrong     = list(range(1,index_correct))
            X['answer']     = random.choice(operators[str(index_correct)])
        else:
            X['condition']  = "lowest"
            index_correct   = random.randint(1,len(operators)-2)
            index_wrong     = list(range(index_correct+1,len(operators)+1))
            X['answer']     = random.choice(operators[str(index_correct)])
            
        temp = []
        for i in index_wrong:
            for j in operators[str(i)]:
                temp.append(j)
        X['choice'] =[X['answer']]
        X['choice'].extend(random.sample(temp,k=3))            
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]
        

    def model_3(self):
        self.QUESTION   = """What is the value stored in x in the followin lines of Java code?
        int x, y, z;
        x = {num[0]};
        y = {num[1]}
        x = y = z = {num[2]}
        """
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
        
        X               = {} 
        X['num']        = [ random.randint(-50,50),
                             random.randint(-50,50),
                             random.randint(-50,50)]
        X['answer']     = X['num'][2]
        X['choice']     = X['num']
        X['choice'].append("Syntax error (illegal expression)")
        
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]
        

    def model_4(self):
        self.QUESTION   = """What is the order of precedence (highest to lowest) of the following operators?
        1. {operator[0]}
        2. {operator[1]}
        3. {operator[2]}
        """
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}",
                            "{choice[4]}",
                            "{choice[5]}",]        
        X               = {}        
        operators       = {
                        "10":["()"],
                        "9":["++","--","!"],
                        "8":["*","/","%"],
                        "7":["+","-"],
                        "6":[">","<","<=",">="],
                        "5":["==","!="],
                        "4":["&&"],
                        "3":["||"],
                        "2":["?:"],
                        "1":["=","+=","-=","/=","*=","%="]
                    }
        index           = random.sample(list(operators.keys()), k=3)
        X['choice']     = []
        X["operator"]   = [random.choice(operators[i]) for i in index]
        for i in index:
            for j in [k for k in index if k !=i]:
                k = [k for k in index if k !=i and k !=j][0]
                X['choice'].append("%d > %d > %d"%(index.index(i)+1,index.index(j)+1,index.index(k)+1))
                if int(i) > int(j) > int(k):
                    X['answer'] = X['choice'][-1]
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]
        

    def model_5(self):
        self.QUESTION   = """What will be the output of the following Java code?
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
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}",
                            "{choice[4]}"]         
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
            return self.model_05()
            
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]
        

    def model_6(self):
        self.QUESTION   = """Suppose x = {num[0]}, y = {num[1]}, and z = {num[2]}. What is the printout of the following statement? (Please indent the statement correctly first.)
            
            if ({num[0]} > {num[3]})
               if ({num[1]} > {num[4]})
                  System.out.print("output1 ");
            else if ({num[2]} > {num[5]})
                  System.out.print("output2 ");
                  System.out.println("output3");

        """
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}",
                            "{choice[4]}"]
        X['num']        = [  random.randint(-10,10),
                             random.randint(-10,10),
                             random.randint(-10,10),
                             random.randint(-10,10),
                             random.randint(-10,10),
                             random.randint(-10,10)]
        
        # # # # code # # # #
        output          = ""
        if (X['num'][0] > X['num'][3]):
           if (X['num'][1] > X['num'][4]):
               output += "output1 "
           elif (X['num'][2] > X['num'][5]):
               output += "output2 "
        output += "output3"        
        # # # # # # # # # #
        X['choice']      = ["output1 ",
                                "output2 ",
                                "output3 ",
                                "output1 output3 ",
                                "output2 output3 "]
        X['answer'] = output
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]
        
    def model_7(self):
        self.QUESTION   = """What is the value of the following expression?
            
            {expression}
            
        """
        self.CHOICES    = [ "true",
                            "false"]

        X['state']      = random.sample(["true","false","true","false"],k=3)
        
        X['o']          = random.sample(["||","&&"],k=2)
        X['expression'] = "{state[0]} {o[0]} {state[1]} {o[1]} {state[2]}".format(**X)
        # calculating the output
        command         = X['expression'].replace("true","True").replace("false","False")
        command         = command.replace("&&","&").replace("||","|")
        X['answer']     = eval(command)
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]
        

    def model_8(self):
        self.QUESTION   = """The following code display __________.
            
            double temperature = {tem};
            
            if (temperature >= 100)
              System.out.println("too hot");
            else if (temperature <= 20)
              System.out.println("too cold");
            else
              System.out.println("just right");

        """
        self.CHOICES    = [ "too hot too cold just right",
                            "just right",
                            "too cold",
                            "too hot"]
        
        X['tem']        = random.randint(-30,250)
        
        # # # # code # # # #
        output          = "too hot too cold just right"
        if (X['tem'] >= 100):   output = "too hot"
        elif (X['tem'] <= 20):  output = "too cold"
        else:                   output = "just right"
        # # # # # # # # # #

        X['answer'] = output
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]
        
   
     
    def model_9(self):
        self.QUESTION   = "If x= {x}, which of the following statement is true? Select all that apply."
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
        DIR             = os.path.join(self.BASE_DIR,'data','booleanexpression.json')
        with open(DIR) as f:
            booleans = json.load(f)
            
        statements      = booleans["1"] + booleans["2"]
        statements     += ['x > y','x >= y','x < y','x < y']
        X['choice']     = []
        X['answer']     = []
        X['x']          = random.randint(0,30)
        for i in range(4):
            [s1,s2]     = random.sample(statements,k=2)
            x           = X['x']
            s1          = s1.replace("y",str(random.randint(0,30)))
            s2          = s2.replace("y",str(random.randint(0,30)))
            X['choice'].append("(%s) is same as (%s)"%(s1,s2))
            s1      = s1.replace("!(","not(").replace("&&","&").replace("||","|")
            s2      = s1.replace("!(","not(").replace("&&","&").replace("||","|")
            X['answer'].append(eval(s1) == eval(s2))

        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]


    def model_10(self):
        self.QUESTION   = """The following code displays __________?
        
        int x = {x};
        
        if ({exp[0]})
          System.out.print("Apple ");
        {{
        if ({exp[1]})
          System.out.print("Banana ");
        else
          System.out.print("Orange");
        }}
        """
        self.CHOICES    = [ "Apple ",
                            "Banana ",
                            "Orange",
                            "Apple Banana ",
                            "Apple Orange",
                            "Banana Orange",
                            "Nothing will be printed"]
        
        statements      = ['x > y || x > z','x > y && x > z']
        statements     += ['not(x > y) || x < z','not(x > y) && x < z']
        statements     += ['x > y || not(x < z)','x < y && not(x < z)']
        statements     += ['not(x > y || x > z)','not(x > y && x > z)']
        
        X['x']          = random.randint(-10,10)
        [s1,s2]         = random.sample(statements,k=2)        
        s1              = s1.replace("y",str(random.randint(-15,15))).replace("z",str(random.randint(-15,15)))
        s2              = s2.replace("y",str(random.randint(-15,15))).replace("z",str(random.randint(-15,15)))
        X['exp']        = [s1, s2]
        # # # code execution # # # #
        x               = X['x']
        s1              = s1.replace("!(","not(").replace("&&","and").replace("||","or")
        s2              = s1.replace("!(","not(").replace("&&","and").replace("||","or")    
        # code
        output          = "Nothing will be printed"
        if eval(s1):
            output = "Apple "
            if eval(s2):
                output += "Banana "
            else:
                output += "Orange"       
        #
        # # # # # # # # # # # # # # #
        X['answer']     = output

        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]



    def model_11(self):
        self.QUESTION   = """The following code displays __________?
        
        int x = {x};
        
        if ({exp[0]})
          x *= -1;  
          System.out.print("Apple ");
        if ({exp[1]})
          System.out.print("Banana ");
        else
          System.out.print("Orange");
        """
        self.CHOICES    = [ "Apple ",
                            "Banana ",
                            "Orange",
                            "Apple Banana ",
                            "Apple Orange",
                            "Banana Orange",
                            "Nothing will be printed"]
        
        statements      = ['x > y || x > z','x > y && x > z']
        statements     += ['not(x > y) || x < z','not(x > y) && x < z']
        statements     += ['x > y || not(x < z)','x < y && not(x < z)']
        statements     += ['not(x > y || x > z)','not(x > y && x > z)']
        
        X['x']          = random.randint(-10,10)
        [s1,s2]         = random.sample(statements,k=2)        
        s1              = s1.replace("y",str(random.randint(-15,15))).replace("z",str(random.randint(-15,15)))
        s2              = s2.replace("y",str(random.randint(-15,15))).replace("z",str(random.randint(-15,15)))
        X['exp']        = [s1, s2]
        # # # code execution # # # #
        x               = X['x']
        s1              = s1.replace("!(","not(").replace("&&","and").replace("||","or")
        s2              = s1.replace("!(","not(").replace("&&","and").replace("||","or")    
        # code
        output          = "Nothing will be printed"
        if eval(s1):    x *= -1;
        output          = "Apple "
        if eval(s2):    output += "Banana "
        else:           output += "Orange"       
        #
        # # # # # # # # # # # # # # #
        X['answer']     = output

        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]



    def model_12(self):
        self.QUESTION   = """Which of the following is the correct expression that \
evaluates to true if the integer x is between {lower} and {upper}. Select all that apply."""

        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]

        statements      = ['x > y', 'x > z','x >= y', 'x >= z']        
        statements     += ['x > y || x > z','x > y && x > z']
        X['choice']     = []
        X['answer']     = []
        X['lower']      = random.randint(0,100)
        X['upper']      = random.randint(X['lower'],100)
        for i in range(len(self.CHOICES)):        
            s               = random.choice(statements)        
            s               = s.replace("y",str(random.randint(0,100))).replace("z",str(random.randint(0,100)))
            X['choice'].append(s)
            s               = s.replace("!(","not(").replace("&&","and").replace("||","or")
            x               = X['lower']+1
            lower_condition = eval(s)
            x               = X['upper']-1
            upper_condition = eval(s)
            X['answer'].append(lower_condition and upper_condition)


        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]



    def model_13(self):
        self.QUESTION   = """The following code will display ______.
        
    class test 
    {{
        public static void main(String args[])
        {{
            int var1 = {num[0]}; 
            int var2 = {num[1]};
            if ((var2 = {num[2]}) == var1)
                System.out.print(var2);
            else 
                System.out.print(++var2);
        }} 
    }}        
        """
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}",
                            "{choice[4]}"]

        X               = {}
        X['choice']     = []        
        X['num']        = [ random.randint(-50,-5),
                            random.randint(-2,5),
                            random.randint(10,50)]
        # # # # # code # # # # #
        if X['num'][1] == X['num'][0]:
            X['answer'] = X['num'][1]
        else:
            X['answer'] = X['num'][2] + 1
        X['choice'].append(X['num'][0])
        X['choice'].append(X['num'][1])
        X['choice'].append(X['num'][2])
        X['choice'].append(X['num'][1] + 1)
        X['choice'].append(X['num'][2] + 1)
        
            
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]



    def model_14(self):
        self.QUESTION   = """The following code will display ______.
        
    class test 
    {{
        public static void main(String args[])
        {{
             int sum = 0;
             for (int i = {lower[0]}, j = {lower[1]}; i < {upper[0]} & j < {upper[1]}; ++i, j = i + 1)
                 sum += i;
            tem.out.println(sum);
        }} 
    }}        
        """
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
        X               = {}
        X['choice']     = []
        
        X['lower']      = [ random.randint(0,3),
                            random.randint(0,3)]
        
        X['upper']      = [ random.randint(4,9),
                            random.randint(4,9)]
        #####
        choices         = [0,0]
        for i,j in zip(range(X['lower'][0],X['upper'][0]),range(X['lower'][1],X['upper'][1])):
            choices[0] += i
            choices[1] += j

        choices.extend([sum(range(X['lower'][0],X['upper'][0])),
                        sum(range(X['lower'][1],X['upper'][1])),
                        sum(range(X['lower'][0],X['upper'][0]+1)),
                        sum(range(X['lower'][1],X['upper'][1]+1))])
        X['answer']     = choices[0]
        if len(set(choices)) == 3:
                choices.append("compilation error")
        elif len(set(choices)) < 3:
            return self.model_14()
        
        X['choice'] = list(set(choices))

        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]


    def model_15(self):
        self.QUESTION   = """Suppose int i = {i}, which of the following 
can be used as an index for array double[] t = new double[{index}]? select all that apply."""
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
        
        X = {}
        X['index']  = random.randint(11,250)
        X['i']      = random.randint(0,X['index']) 
        
        choices     = []
        choices.append(["i",True if X['i'] in range(X['index']) else False])
        choices.append(["i*2",True if X['i']*2 in range(X['index']) else False])
        t = float(random.random()*100)
        choices.append(["(int) (i + %2.2f)"%t,True if X['i'] + t in range(X['index']) else False])
        t = random.randint(1,100)       
        choices.append(["i+%d"%t,True if X['i']+t in range(X['index']) else False])
        choices.append(["Math.random() * 10",False])
        choices.append(["(int) Math.random() * 10", True]) 
        choices.append(["(int) Math.random() * -10", True]) 
        choices.append(["(int) (Math.random() * 10)", True]) 
        choices.append(["(int) (Math.random() * -10)", False]) 
        choices.append(["(int) (Math.random() * 10)", True]) 
        choices.append(["(int) (Math.random() * -10)", False]) 
        
        temp        = random.sample(choices, k=5)
        X['choice'] = [i[0] for i in temp]
        ANSWER = [i[1] for i in temp]

        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                ANSWER]



    def model_16(self):
        self.QUESTION   = """The following code will display ______.
        
        for (int i = {start}; i < {end}; i++)
            if (i % {divisor} == {remainder})
                System.out.print(i + " ");
        """
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
        X               = {}
        X['start']      = random.randint(0,5)
        X['end']        = random.randint(12,21)
        X['divisor']    = random.randint(2,6)
        X['remainder']  = random.randint(0,X['divisor']-1)
        def fun(s,e,d,r):
            t = ""
            for i in range(s,e):
                if (i%d) == r:
                    t += "%d "%i
            return t
        
        choices         = []
        choices.append(fun(X['start'],X['end'],X['divisor'],X['remainder']))                #(p+q)*q + r
        choices.append(fun(X['start'],X['end']+X['divisor'],X['divisor'],X['remainder']))   #(p-q)*q + r
        choices.append(fun(X['start'],X['end']-X['divisor'],X['divisor'],X['remainder']))   
        choices.append(fun(X['start'],X['end'],X['divisor'],X['remainder']-1))
        choices.append(fun(X['start'],X['end'],X['divisor'],X['remainder']+1))
        choices.append(fun(X['start'],X['end'],X['divisor']+1,X['remainder']+1))
        choices.append(fun(X['start'],X['end'],X['divisor']-1,X['remainder']+1))
        
        X['answer']     = choices[0]
        if len(set(choices)) < 5 or choices[0]=='':
            return self.model_16()
        else:
            choices = list(set(choices))
            
        if '' in choices:
            choices.remove('')
        X['choice']     = random.sample(choices,4)
        if X['answer'] not in X['choice']:
            X['choice'][-1] = X['answer']
        
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]



    def model_17(self):
        self.QUESTION   = """In the following code, you should fill in the blank with which return type?
        

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
        self.CHOICES    = [ "int",
                            "double",
                            "boolean",
                            "char",
                            "void"]
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
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]




    def model_18(self):
        
        self.QUESTION   = """The following code will display ______.
        
    int arr[] = new int[{num}];
    {code}
    System.out.println(arr{index});
        """
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}",
                            "{choice[4]}",
                            "{choice[5]}"]
        
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
            return self.model_18()
        
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]


    def model_19(self):
        
        self.QUESTION   = """The following code will display ______.
        
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
        
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}",
                            "{choice[4]}"]
        X           = {}
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
        
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]
        
        


    def model_20(self):
        
        self.QUESTION   = """The following code will display ______.
        
		double[] myList = {{ {list} }};
		double {type} = myList[0];
		int indexOf{type} = 0;
		for ({loop}) {{
			if (myList[i] > {type}) {{
				{type} = myList[i];
				indexOf{type} = i;
			}}
		}}
        System.out.println(indexOf{type});       
        """

        self.CHOICES    = [ "0",
                            "1",
                            "2",
                            "3",
                            "4",
                            "5"]
        X           = {}
        ######## question types
        X['type'] = random.choice(["max", "min"])  
        direction = random.choice(["FromStart","FromEnd"])
        if direction == "FromStart":
            X['loop'] = "int i = 0; i < myList.length; i++"
        else:
            X['loop'] = "int i = myList.length-1; i >= 0; i--"
            

       # creating list
        List        = random.choices(list(range(0,10)),k=3)
        List        = List + List
        X['list']   = str(List)[1:-1]
        ### 
        if X['type'] == "min":
            temp = [i for i, j in enumerate(List) if j == min(List)]
            if direction == "FromStart":
                X['answer'] = min(temp)
            else:
                X['answer'] = max(temp)
        else:
            temp = [i for i, j in enumerate(List) if j == max(List)]
            if direction == "FromStart":
                X['answer'] = min(temp)
            else:
                X['answer'] = max(temp)            
                     

        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]
        


    def model_21(self):
        
        self.QUESTION   = "Which of the following is correct? "
        
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}",
                            "{choice[4]}"]
        Type            = ["double", 
                                 "float",
                                 "int",
                                 "long",
                                 "short",
                                 "char",
                                 "boolean"]
        c           = {}
        correct     = [ "{type}[] a = new {type}[{num}];"]
        wrong       = [ "{type}[] a = new {type}({num});",
                        "{type}[] a = new {type}{{{num}}};",
                        "{type}[] a = {type}({num});",
                        "{type}[] a = {type}{{{num}}};",
                        "{type}[] a = new ({num});",
                        "{type}[] a = new {{{num}}};",
                        "{type} a = new {type}({num});",
                        "{type} a = new {type}{{{num}}};",
                        "{type} a = {type}({num});",
                        "{type} a = {type}{{{num}}};",
                        "{type} a = new ({num});",
                        "{type} a = new {{{num}}};",
                        "{type}() a = new {type}({num});",
                        "{type}() a = new {type}{{{num}}};",
                        "{type}() a = {type}({num});",
                        "{type}() a = {type}{{{num}}};",
                        "{type}() a = new ({num});",
                        "{type}() a = new {{{num}}};",
                        "{type} a[] = new {type}({num});",
                        "{type} a[] = new {type}{{{num}}};",
                        "{type} a[] = {type}({num});",
                        "{type} a[] = {type}{{{num}}};",
                        "{type} a[] = new ({num});",
                        "{type} a[] = new {{{num}}};",
                        "{type}[] = new {type}[{num}];",
                        "{type}[] = new {type}({num});",
                        "{type}[] = new {type}{{{num}}};",
                        "{type}[] = {type}({num});"]
        X           = {} 
        c['type']   = random.choice(Type)
        c['num']    = random.randint(2,20)
        X['answer'] = correct[0].format(**c)
        choices     = correct + random.sample(wrong,k=4)
        X['choice'] = []
        for i in choices:
            c['type']   = random.choice(Type)
            c['num']    = random.randint(2,20)            
            X['choice'].append(i.format(**c))
            
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]
       
                    
if __name__ == "__main__":
    
    variabletype = VariableType()
    for _ in range(1):_ = variabletype.generate()

