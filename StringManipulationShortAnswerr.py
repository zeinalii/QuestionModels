

# Short Answer
""" The answer should be a string with a maximum length of 25 characters"""

import random
import string 

class StringManipulationShortAnswer:
    def __init__(self):
        self.QUESTION   = """What is the result of "{string}".{method}{indeces}?"""
        self.ANSWER   = "{answer}"
        
    def getQuestion (self):
        self.QUESTION
        
    def getAnswer (self):
        self.ANSWER
        
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
        print("\nAnswer: ", self.ANSWER.format(**X))
        
        return [self.QUESTION.format(**X),
                self.ANSWER.format(**X)]
    
        # < --------------------------------------------------- >
    def length(self):
        """
            What is the result of "vrQVF".length()?
            
            Answer:  5      
        """           
        X           = {}
        X['method'] = "length"
        X['string'] = self.randomString(random.randint(5,10))
        X['indeces'] = "()"
        X['answer'] = str(len(X['string']))
        return self.GenerateQuestion(X)
        # < --------------------------------------------------- >
    def charAt(self):
        """
            What is the result of "MQhgP".charAt(2)?
            
            Answer:  h        
        """   
        X           = {}
        X['method'] = "charAt"
        X['string'] = self.randomString(random.randint(5,10))
        a           = random.randint(0,len(X['string'])-1)
        X['indeces'] = ("({})").format(a)
        X['answer'] = X['string'][a]
        return self.GenerateQuestion(X)
        # < --------------------------------------------------- >
    def contains(self):
        """
            What is the result of "zoimCX".contains("io")?
            
            Answer:  false        
        """           
        X           = {}
        X['method'] = "contains"
        X['string'] = self.randomString(random.randint(6,10))
        a = random.randint(0, len(X['string']) - 3)
        b = random.randint(1,3)
        substring = X['string'][a:a+b]
        if (random.random()< 0.2):
            substring = substring.lower()
        elif (random.random() <0.2): 
            substring = substring.upper()
        elif (random.random() <0.2): 
            substring = substring[::-1]
        elif (random.random() <0.2): 
            substring = substring + random.choice(string.ascii_lowercase +
                                                       string.ascii_uppercase)
        elif (random.random() <0.2): 
            substring = random.choice(string.ascii_lowercase +
                                                       string.ascii_uppercase) + substring 
        X['indeces']= ("(\"{}\")").format(substring)
        if X['string'].find(substring) != -1:
            X['answer'] = "true"           
        else:
            X['answer'] = "false" 
        return self.GenerateQuestion(X)
        # < --------------------------------------------------- >
    def equals(self):
        """
            What is the result of "LjklSzUG".equals("LjklSzUG")?
            
            Answer:  true        
        """       
        X           = {}
        X['method'] = "equals"
        X['string'] = self.randomString(random.randint(5,10))
        substring = X['string']
        if (random.random()< 0.2):
            substring = substring.lower()
        elif (random.random() <0.2): 
            substring = substring.upper()
        elif (random.random() <0.2): 
            substring = substring[::-1]
        elif (random.random() <0.2): 
            substring = substring[0:random.randint(1,len(X['string']))]
            
        X['indeces']= ("(\"{}\")").format(substring)
        if X['string']  == substring:
            X['answer'] = "true"           
        else:
            X['answer'] = "false"         
        return self.GenerateQuestion(X)
        # < --------------------------------------------------- >
    def replace(self):
        """
            What is the result of "bljlv".replace("l","@")?
            
            Answer:  b@j@v4        
        """        
        X           = {}
        X['method'] = "replace"
        s1 = self.randomString(random.randint(1,2))
        s2 = self.randomString(random.randint(1,3))
        s3 = self.randomString(random.randint(1,2))
        s4 = self.randomString(random.randint(1,2))
        X['string'] = s1 + s2 + s3 + s2 + s4
        replaceString = random.choice("!@#$^*-")
        X['indeces']= ("(\"{}\",\"{}\")").format(s2,replaceString)
        X['answer'] = X['string'].replace(s2,replaceString)
        return self.GenerateQuestion(X)
        # < --------------------------------------------------- >
    def indexOf(self):
        """
        Example: 
                What is the result of "wlgqlYG".indexOf("l",4)?
                
                Answer:  4        
        """
        X           = {}
        X['method'] = "indexOf"
        s1 = self.randomString(random.randint(1,2))
        s2 = self.randomString(random.randint(1,2))
        s3 = self.randomString(random.randint(1,2))
        s4 = self.randomString(random.randint(1,2))
        X['string'] = s1 + s2 + s3 + s2 + s4
        Index = random.randint(0,len(X['string']))
        X['indeces']= ("(\"{}\",{})").format(s2,Index)
        X['answer'] = X['string'].find(s2,3)
        return self.GenerateQuestion(X)

    def generate(self):
        methods = ['length',
                   'charAt',
                   'contains',
                   'equals',
                   'replace',
                   'indexOf']
        method = random.choice(methods)
        if method == 'length':
            return self.length()
        elif method == 'charAt':
            return self.charAt()        
        elif method == 'contains':
            return self.contains()        
        elif method == 'equals':
            return self.equals()
        elif method == 'replace':
            return self.replace()
        elif method == 'indexOf':
            return self.indexOf()











        
if __name__ == "__main__":
    
    shortanswer = StringManipulationShortAnswer()
    
    # We can call them separately 
    _ = shortanswer.length()
        """
            What is the result of "vrQVF".length()?
            
            Answer:  5      
        """        
    _ = shortanswer.charAt()
        """
            What is the result of "MQhgP".charAt(2)?
            
            Answer:  h        
        """   
    _ = shortanswer.contains()
        """
            What is the result of "zoimCX".contains("io")?
            
            Answer:  false        
        """
    _ = shortanswer.equals()
        """
            What is the result of "LjklSzUG".equals("LjklSzUG")?
            
            Answer:  true        
        """
    _ = shortanswer.replace()
        """
            What is the result of "bljlv".replace("l","@")?
            
            Answer:  b@j@v4        
        """
    _ = shortanswer.indexOf()
        """
        Example: 
                What is the result of "wlgqlYG".indexOf("l",4)?
                
                Answer:  4        
        """
    # calling randomly
    _ = shortanswer.generate()

     