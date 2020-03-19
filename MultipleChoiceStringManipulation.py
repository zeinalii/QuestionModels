


import random
import string 

class MultipleChoiceStringManipulation:
    def __init__(self,QUESTION,CHOICES):
        self.QUESTION   = QUESTION
        self.CHOICES    = CHOICES
        
    def getQuestion (self):
        self.QUESTION
        
    def getChoices(self):
        return self.CHOICES
    
    def generateSubstringQuestion(self):
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
        X           = {}
        X['method'] = "substring"                                            # method we want to use
        X['string'] = self.randomString(random.randint(5,10))                # generating a random un-repeated string with length of stringLength
        a           = random.randint(1,len(X['string'])-1)                   # lower bound   1<=a<=len(STRING)-1
        b           = random.randint(a,len(X['string'])-1)                   # upper bound a <=b<=len(STRING)
        X['indeces']= (a,b)                                                  # creating (a,b)  
        #  choices
        if (X['string'][a:b] == ""):
            X['a']  = "an empty string"          #  choice a is                                 
            X['b']  = "Error"                    #  choice b                                
        else:
            X['a']  =   X['string'][a:b]         #  choice a
            X['b']  = X['string'][a+1:b+1]       #  choice b
        X['c'] = X['string'][a: b+1]             #  choice c
        if len(X['string']) == b+1:
            X['d'] = X['string'][a-2: b+1]       #  choice d
        else:
            if X['string'][a+1:b+2] == "":
                X['d'] = "an empty string"
            else:
                X['d'] = X['string'][a+1:b+2]
        for i in range(4):
            for j in range(i+1,4):
                if X['abcd'[i]] == X['abcd'[j]]:
                    print("\n<--ERROR-->\n")
        return self.GenerateQuestion(X)


    def randomString(self,stringLength=10):
        """Generate a random string of fixed length """
        letters = string.ascii_uppercase + string.ascii_lowercase
        for i in range(len(letters) - stringLength):
            letters = letters.replace(random.choice(letters),"")
        return ''.join(random.sample(letters,len(letters)))
    

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

    def generateIndexOfQuestion(self):
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
        X['string'] = self.randomString(random.randint(5,10))              # generating a random un-repeated string with length of stringLength
        i           = random.randint(1,len(X['string'])-1)                 # lower bound   1<=a<=len(STRING)-1
        a           = X['string'][i:i+2]
        b           = random.randint(0,len(X['string'])-1)                 # upper bound a <=b<=len(STRING)
        X['indeces']= (a,b)                                                # creating (a,b)         
        #  choices
        try: 
            X['a'] = X['string'].index(a,b)
            X['b'] = X['a'] - 1
            X['c'] = X['a'] + 1
            if X['c'] == len(X['string']):
                X['d'] = -1
            else:
                X['d'] = X['a'] + 2
        except ValueError:
            X['a'] = -1
            X['b'] = X['string'].index(a)
            X['c'] = X['b'] + 1
            if X['c'] == len(X['string']):
                X['d'] = -1
            else:
                X['d'] = X['b'] + 2
        return self.GenerateQuestion(X)
    def generate(self):
        n = random.randint(1,2)
        if n == 1:
            return self.generateIndexOfQuestion()
        if n== 2:
            return self.generateSubstringQuestion()











if __name__ == "__main__":
    
    q = """What is the return value of "{string}".{method}{indeces}?"""
    c = [   "{a}",
            "{b}",
            "{c}",
            "{d}"]

    stringmanipulation = MultipleChoiceStringManipulation(q,c)
    [QUESTION, CHOICES, ANSWER] = stringmanipulation.generateIndexOfQuestion()
    [QUESTION, CHOICES, ANSWER] = stringmanipulation.generateSubstringQuestion()
    
    """
    result:
        What is the return value of "DeEBP".indexOf('EB', 3)?
        .  -1
        .  2
        .  3
        .  4
        
        Answer:  -1
        
        
        What is the return value of "jdpayub".substring(4, 6)?
        .  yu
        .  ub
        .  yub
        .  payub
        
        Answer:  yu
    """

     