


from templates.QuestionModels import MultipleChoice, NamingConvention
import os, random, json, string
import numpy as np


#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

class model_1(MultipleChoice):
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs = [
                'substring',
                ]    
    QUESTION = """What is the return value of "{string}".{method}{indeces}?"""
    CHOICES    = ["{a}",
                  "{b}",
                  "{c}",
                  "{d}"]
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        DIR     = os.path.join(self.BASE_DIR,'data','words.json')
        with open(DIR) as f:
            self.WORDS = json.load(f)
            
    def model(self):
        """ Generate random multiple choice questions
        for example:


        What is the return value of "CTmAbUotca".substring(4, 9)?
            .  bUotc
            .  Uotca
            .  bUotca
            .  mAbUotca

            Answer:  bUotc


            output is a list containing : [Question, Choices, Answer]
            """
        X               = {}
        X['method']     = "substring"  # method we want to use
        X['string']     = self.randomWord()  # generating a random un-repeated string with length of stringLength
        a               = random.randint(1, len(X['string']) - 1)  # lower bound   1<=a<=len(STRING)-1
        b               = random.randint(a, len(X['string']) - 1)  # upper bound a <=b<=len(STRING) -1
        X['indeces']    = (a, b)  # creating (a,b)
        #  choices
        if (X['string'][a:b] == ""):
            X['a'] = "an empty string"  # choice a is theCorrect answer
            X['b'] = "Syntax error (illegal expression)"  # choice b
        else:
            X['a'] = X['string'][a:b]  # choice a
            X['b'] = X['string'][a + 1:b + 1]  # choice b
        X['c'] = X['string'][a: b + 1]  # choice c
        if len(X['string']) == b + 1:
            X['d'] = X['string'][a - 2: b + 1]  # choice d
        else:
            if X['string'][a + 1:b + 2] == "":
                X['d'] = "an empty string"
            else:
                X['d'] = X['string'][a + 1:b + 2]
        X['answer'] = X['a']
        if len(set([X['a'], X['b'], X['c'], X['d']])) != 4:
            return self.model()
        else:
            return X

    def randomWord(self):
        return random.choice(self.WORDS['words'])   

#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

class model_2(MultipleChoice):
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs = [
                'indexOf',
                ]    
    QUESTION = """What is the return value of "{string}".{method}{indeces}?"""
    CHOICES    = ["{a}",
                  "{b}",
                  "{c}",
                  "{d}"]
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        DIR     = os.path.join(self.BASE_DIR,'data','words.json')
        with open(DIR) as f:
            self.WORDS = json.load(f)
            
    def model(self):
        """ Generate random multiple choice questions
        
        for example:
        What is the return value of "JTKqE".indexOf('qE', 0)?
        .  3
        .  2
        .  4
        .  5
        
        Answer:  3     
        """
        X           = {}
        X['method'] = "indexOf"                                            # method we want to use
        X['string'] = self.randomWord()                                    # generating a random un-repeated string with length of stringLength
        i           = random.randint(0,len(X['string'])-1)                 # lower bound   1<=a<=len(STRING)-1
        if random.random() < 0.8:                                          #the character is inside the string
            a           = X['string'][i]
            X['indeces']= "('{}')".format(a) 
            X['a']      = X['string'].index(a)
            X['b']      = X['a'] - 1
            X['c']      = X['a'] + 1
            X['d']      = X['a'] + 2
                                                     
        else: 
            a           = X['string'][i].lower() if X['string'][i].isupper() else X['string'][i].upper()
            X['indeces']= "('{}')".format(a) 
            X['a']      = -1
            X['b']      = "false" 
            X['c']      = i
            if X['c'] == len(X['string']):
                X['d']  = i - 1
            else:
                X['d']  = i + 1      
        X['answer'] = X['a']
        if len(set([X['a'],X['b'],X['c'],X['d']])) != 4: 
            return self.model()
        else:
            return X

    def randomWord(self):
        return random.choice(self.WORDS['words'])   

#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

class model_3(MultipleChoice):
    
    QUESTION   = "The expression {expression} is evaluated to"
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
    
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

class model_4(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs = [
                'remainder',
                ]   

    QUESTION   = "Which of the following values results in {value}?"
    CHOICES    = [ "{choice[0]}",
                    "{choice[1]}",
                    "{choice[2]}",
                    "{choice[3]}",
                    "{choice[4]}"]     
    def model(self):
        X               = {}
        X['choice']     = []
        results = []
        while len(results) < 5:
            c = random.randint(1,9)
            b = random.randint(1,15)
            v = random.randint(1,b)
            a = c * b + v
            if (a%b) not in results:
                X['choice'].append("{0} % {1}".format(a,b))
                results.append(a%b)                
        i               = random.choice(range(len(results)))
        X['value']      = results[i]
        X['answer']     = X['choice'][i]
        
        return X
    
        
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

class model_5(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs = [
                'ASCII',
                ]   

    CHOICES    = [ "{choice[0]}",
                    "{choice[1]}",
                    "{choice[2]}",
                    "{choice[3]}"]
    QUESTION   = "Note that the ASCII value for character {character} is {ASCII}. \
What does the expression \"{character}\" + 1 evaluate to?"
  
    def model(self):
        X       = {}
        X['character']  = random.choice(string.ascii_uppercase)
        X['ASCII']      = ord(X['character'])
        X['choice']     = [ X['ASCII'] + 1,
                            chr(X['ASCII'] + 1),
                            X['character'] + '1',
                            "Syntax error (illegal expression)"]
        X['answer']     = X['character'] + '1'


        return X
    
    
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

class model_6(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs = [
                'Final',
                'constant',
                ]   

    CHOICES    = [ "final double {variable} = {value:2.2f}",
                               "final {variable} = {value:2.2f}",
                               "final long {variable} = {value:2.2f}",
                               "double {variable} = {value:7.2f}"]
    QUESTION   = """To declare a constant {variable} inside a method with value {value:2.2f}, you write:"""

    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        DIR     = os.path.join(BASE_DIR,'data','javanameconvention.json')
        with open(DIR) as f:
            self.name = json.load(f)
            
            
    def model(self):
        X               = {}
        X['value']      = random.random()*100
        X['variable']   = random.choice(self.name['adjective']).upper() +\
                            "_" + random.choice(self.name['descriptiveName']).upper()
        X['answer']     = self.CHOICES[0].format(**X)
        return X
        


#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

class model_7(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs = [
                'DoubleToInteger',
                'decimal',
                ]   

    CHOICES    = [ "( int )( {value[0]:7.4f} * {value[1]} ) / {value[1]}",
                            "( int )( {value[0]:7.4f} * {value[1]} ) / {value[1]}.0",
                            "( int )( {value[0]:7.4f} * {value[1]} / {value[1]} )",
                            "( int )( {value[0]:7.4f} ) * {value[1]} / {value[1]}.0"]
    QUESTION   = "Which of the following expression results in {question}?"
    ANSWER     = "( int )( {value[0]:7.4f} * {value[1]} ) / {value[1]}"
    
      
            
    def model(self):
        X           = {}
        X['value']  = [random.random()*100,            # generating a random number between 0 and 100
                         random.choice([10,100,1000])] # choosing values between 10,100,1000
        
        X['question'] = int(X['value'][0]*X['value'][1])/X['value'][1]
        
        X['answer']     = self.CHOICES[0].format(**X)
        return X
    
    
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

class model_8(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs        = [
                        'boolean',
                        ]   

    CHOICES         = [ "{choice[0]}",
                    "{choice[1]}",
                    "{choice[2]}",
                    "{choice[3]}"]
    QUESTION        = "The expression {expression} is equivalent to"
    
    def __init__(self):
        BASE_DIR    = os.path.dirname(os.path.dirname(__file__))
        DIR         = os.path.join(BASE_DIR,'data','booleanexpression.json')
        with open(DIR) as f:
            self.booleanList = json.load(f)
            
            
    def model(self):
        X           = {}
        i           = random.choice(['1','2'])
        X['expression'] , X['choice'] = random.sample(self.booleanList[i],2)
        X['choice'] = [X['choice']]
        X['choice'].extend(random.sample(self.booleanList['-' + i],3))
        X['answer'] = X['choice'][0]
        return X
    
    
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

class model_9(MultipleChoice):
    
    TYPE = "multiplechoice_MultiAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs        = [
                        'boolean',
                        ]   

    CHOICES         = [ "A and B are equivalent",
                                   "A and C are equivalent",
                                   "B and C are equivalent",
                                   "None of the expressions are equivalent"]
    QUESTION        = """Considering the following piece of code, select all the true choices.
Boolean A = {expression[0]};
Boolean B = {expression[1]};
Boolean C = {expression[2]};
"""
    shuffle = False       

    def __init__(self):
        BASE_DIR    = os.path.dirname(os.path.dirname(__file__))
        DIR         = os.path.join(BASE_DIR,'data','booleanexpression.json')
        with open(DIR) as f:
            self.booleanList = json.load(f)
            
    def model(self):
        X               = {}
        temp            = random.choice(['1','2'])        
        X['expression'] = random.sample(self.booleanList[temp] ,2)
        X['expression'].append(random.choice(self.booleanList['-' + temp]))
        random.shuffle(X['expression'])
        ANSWERs = []
        for i in range(len(X['expression'])):
            for j in range(i+1,len(X['expression'])):
                if (X['expression'][i] in self.booleanList[temp]) and \
                    (X['expression'][j] in self.booleanList[temp]):
                        ANSWERs.append(True)
                else:
                    ANSWERs.append(False)
        if True in ANSWERs:
            ANSWERs.append(False)
        else:
            ANSWERs.append(True)
            
        X['answer'] =  ANSWERs
            
        return X    
    
    
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

class model_10(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs        = [
                        'boolean',
                        ]   

    CHOICES         = [ " banana",
                        " apple",
                        " apple orange",
                        " orange",
                        " apple banana",
                        " apple apple"]
    QUESTION        = """Suppose x = {x}, y = {y}, and z = {z}. What is the printout of the following statement? Hint: Indent the statement
correctly first.

String fruit = "unassigned";
if( x > 0 )
{{
    fruit = "apple";
if( y > 0 )
    System.out.print( " " + fruit );
else if( z > 0 )
    fruit = "orange";
    System.out.print( " " + fruit );

}}
else
    fruit = "banana";
    System.out.println( " " + fruit ); 
    """
    
            
    def model(self):
        X           = {}
        X['x']  = random.randint(-1,2)
        X['y']  = random.randint(-1,1)
        X['z']  = random.randint(-1,1)
        
        def temp(x,y,z):
            fruit = "unassigned"
            PrintString = ""
            if (x>0):
                fruit = "apple"
                if y> 0:
                    PrintString += " " + fruit
                elif z>0:
                    fruit = "orange"
                PrintString += " " + fruit
            else:
                fruit = "banana"
                PrintString += " " + fruit
            return PrintString
        
        X['answer'] = temp(X['x'],X['y'],X['z'])
        if X['answer'] not in self.CHOICES:
            self.CHOICES[4] = X['answer']            
        return X    
    


#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

class model_11(NamingConvention):
    
    TYPE = "multiplechoice_MultiAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs        = [
                        'NamingConvention',
                        ]   

    CHOICES         = ["a. class name",
                       "b. method name",
                       "c. variable name",
                       "d. none"
                       ]
    
    QUESTION        = """In the following peice of code, which identifier's name is \
        chosen incorect based on the java naming convention. Select all that apply.
        
public class {class[0]} {{
        public double void {method[0]} (double x) {{
                return (x*x + 1);
                }}
       public static void main(String[] args) {{
       double {variable[0]};
       System.out.println({method[0]}());
       }}
}}
        """
    shuffle = False
            
    def model(self):
        X                = {} 
        X['method']      = self.generateMethod()
        X['variable']    = self.generateVariable()
        X['class']       = self.generateClass()
        ANSWER           = [X[i][1] for i in X]
        if True not in ANSWER: ANSWER.append(True)  
        else : ANSWER.append(False)
        X['answer']     = ANSWER
        return X    
    

#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

class model_12(NamingConvention):
    
    TYPE = "multiplechoice_MultiAnswer"
    DIFFICULTY_LEVEL = 1 #1-3
    KEYWORDs        = [
                        'NamingConvention',
                        ]   

    CHOICES         = [ "{choice[0]}",
                          "{choice[1]}",
                          "{choice[2]}",
                          "{choice[3]}"]
    
    QUESTION        = "According to Java naming convention, \
which of the following names can be {identifier}?"
    shuffle = False
    def model(self):
        X               = {} 
        X['choice']     = []
        X['answer']     = []
        X['identifier'] = random.choice(['class','variable','method'])
        if X['identifier'] == "class":
            for i in range(4):
                choice, answer  = self.generateClass()
                X['choice'].append(choice)
                X['answer'].append(answer)
        elif X['identifier'] == "variable":
            for i in range(4):
                choice, answer  = self.generateVariable()
                print(choice,answer)
                X['choice'].append(choice)
                X['answer'].append(answer)
        else:
            for i in range(4):
                choice, answer  = self.generateMethod()
                X['choice'].append(choice)
                X['answer'].append(answer)                

        return X    
        
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

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
     
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

class model_14(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        'precedence',
                        'operator',
                        ]   

    CHOICES         = [ "{choice[0]}",
                    "{choice[1]}",
                    "{choice[2]}",
                    "{choice[3]}"]
    
    QUESTION        = "Which of the following have {condition} precedence?"
    shuffle = True
    def model(self):
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

        return X    
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

class model_15(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        'value Stored in variable',
                        ]   

    CHOICES         = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
    
    QUESTION        = """What is the value stored in x in the followin lines of Java code?
        int x, y, z;
        x = {num[0]};
        y = {num[1]}
        x = y = z = {num[2]}
        """
    shuffle = True
    def model(self):
        
        X               = {} 
        X['num']        = [ random.randint(-50,50),
                             random.randint(-50,50),
                             random.randint(-50,50)]
        X['answer']     = X['num'][2]
        X['choice']     = X['num']
        X['choice'].append("Syntax error (illegal expression)")
          

        return X        
    

##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#
class model_16(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        'precedence',
                        ]   

    CHOICES         = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}",
                            "{choice[4]}",
                            "{choice[5]}"] 
    
    QUESTION        = """What is the order of precedence (highest to lowest) of the following operators?
        1. {operator[0]}
        2. {operator[1]}
        3. {operator[2]}
        """
    shuffle = True
    def model(self):
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
        return X          
#
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#
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


##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#
class model_18(MultipleChoice):
    
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
    
    QUESTION        = """Suppose x = {num[0]}, y = {num[1]}, and z = {num[2]}. What is the printout of the following statement? (Please indent the statement correctly first.)
            
            if ({num[0]} > {num[3]})
               if ({num[1]} > {num[4]})
                  System.out.print("output1 ");
            else if ({num[2]} > {num[5]})
                  System.out.print("output2 ");
                  System.out.println("output3");

        """
    shuffle = False
    def model(self):
        X               = {} 
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

        return X      
#
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

class model_19(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "true",
                            "false"]
    
    QUESTION        = """What is the value of the following expression?
            
            {expression}
            
        """
    shuffle = False
    def model(self):
        X               = {} 
          
        X['state']      = random.sample(["true","false","true","false"],k=3)
        
        X['o']          = random.sample(["||","&&"],k=2)
        X['expression'] = "{state[0]} {o[0]} {state[1]} {o[1]} {state[2]}".format(**X)
        # calculating the output
        command         = X['expression'].replace("true","True").replace("false","False")
        command         = command.replace("&&","&").replace("||","|")
        X['answer']     = eval(command)
        return X        
    

##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#
class model_20(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         =  [ "too hot too cold just right",
                            "just right",
                            "too cold",
                            "too hot"]
    
    QUESTION        = """The following code display __________.
            
            double temperature = {tem};
            
            if (temperature >= 100)
              System.out.println("too hot");
            else if (temperature <= 20)
              System.out.println("too cold");
            else
              System.out.println("just right");

        """
    shuffle = True
    def model(self):
        X               = {} 
          
        X['tem']        = random.randint(-30,250)
        
        # # # # code # # # #
        output          = "too hot too cold just right"
        if (X['tem'] >= 100):   output = "too hot"
        elif (X['tem'] <= 20):  output = "too cold"
        else:                   output = "just right"
        # # # # # # # # # #

        X['answer'] = output
        return X          
#
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#
class model_21(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
    
    QUESTION        = "If x= {x}, which of the following statement is true? Select all that apply."
    shuffle = True
    
    def __init__(self):
        BASE_DIR    = os.path.dirname(os.path.dirname(__file__))
        DIR         = os.path.join(BASE_DIR,'data','booleanexpression.json')
        with open(DIR) as f:
            self.booleanList = json.load(f)
            
    def model(self):
        X = {}
        statements      = self.booleanList["1"] + self.booleanList["2"]
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

        return X   


#
#
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

class model_22(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "Apple ",
                            "Banana ",
                            "Orange",
                            "Apple Banana ",
                            "Apple Orange",
                            "Banana Orange",
                            "Nothing will be printed"]
    
    QUESTION        = """The following code displays __________?
        
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
    shuffle = False
    def model(self):
        X               = {} 
          
        
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
        return X  

#
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#
class model_23(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "Apple ",
                            "Banana ",
                            "Orange",
                            "Apple Banana ",
                            "Apple Orange",
                            "Banana Orange",
                            "Nothing will be printed"]
    
    QUESTION        = """The following code displays __________?
        
        int x = {x};
        
        if ({exp[0]})
          x *= -1;  
          System.out.print("Apple ");
        if ({exp[1]})
          System.out.print("Banana ");
        else
          System.out.print("Orange");
        """
    shuffle = False
    def model(self):
        X               = {} 
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
          

        return X          

##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#
class model_24(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
    
    QUESTION        = """Which of the following is the correct expression that \
evaluates to true if the integer x is between {lower} and {upper}. Select all that apply."""

    shuffle = False
    def model(self):
        X               = {} 
          
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

        return X   

#
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#
class model_25(MultipleChoice):
    
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
    shuffle = True
    
    def model(self):
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
        return X  
#    
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#
class model_26(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
    
    QUESTION        = """The following code will display ______.
        
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
    shuffle = True
    def model(self):
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
            return self.model()
        
        X['choice'] = list(set(choices))

        return X          

##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#
class model_27(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
        
    
    QUESTION        = """Suppose int i = {i}, which of the following 
can be used as an index for array double[] t = new double[{index}]? select all that apply."""

    shuffle = False
    def model(self):
        X               = {} 
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
        X['answer'] = [i[1] for i in temp]
        return X   



##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#
class model_28(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
    
    QUESTION        = """The following code will display ______.
        
        for (int i = {start}; i < {end}; i++)
            if (i % {divisor} == {remainder})
                System.out.print(i + " ");
        """
    shuffle = True
    
    
    def model(self):
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
            return self.model()
        else:
            choices = list(set(choices))
            
        if '' in choices:
            choices.remove('')
        X['choice']     = random.sample(choices,4)
        if X['answer'] not in X['choice']:
            X['choice'][-1] = X['answer']
        
          

        return X  
#
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#
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

##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#
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




#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

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

##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#
class model_32(MultipleChoice):
    
    TYPE = "multiplechoice_SingleAnswer"
    DIFFICULTY_LEVEL = 1 
    KEYWORDs        = [
                        '',
                        ]   

    CHOICES         = [ "0",
                        "1",
                        "2",
                        "3",
                        "4",
                        "5"]

    QUESTION        = """The following code will display ______.
        
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
    shuffle = True
    def model(self):
        X               = {} 
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
          

        return X  
#
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#
class model_33(MultipleChoice):
    
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
    
    QUESTION        = "Which of the following is correct? "
    shuffle = True
    def model(self):
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
                      

        return X  


        
if __name__=="__main__":
    pass
    