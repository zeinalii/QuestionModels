import random
import json
import os



class NamingConvention:
    def __init__(self):
        BASE_DIR    = os.path.dirname(os.path.dirname(__file__))
        DIR         = os.path.join(BASE_DIR,'data','javanameconvention.json')
        with open(DIR) as f:
            self.name = json.load(f)
        self.template   = """In the following peice of code, which identifier's name is \
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
        self.choice = ["a. class name",
                       "b. method name",
                       "c. variable name",
                       "d. none"
                ]
            
    # < --------------------- >
    def get_correct_class_name(self):
        return random.choice(self.name['name'])
    
    
    def get_wrong_class_name(self):
        if random.random() < 0.3:
            return random.choice(self.name['name']).lower()
        elif random.random() < 0.3:
            return random.choice(self.name['name']).upper()
        elif random.random() < 0.3:
            return random.choice(self.name['adjective']).lower()
        elif random.random() < 0.3:
            return random.choice(self.name['reservedWords']).lower()
        else:
            return random.choice(self.name['verb'])
        
     
    def get_correct_variable_name(self):
        if random.random() < 0.3:
            return random.choice(self.name['descriptiveName']).lower()
        else:
            return random.choice(self.name['name']).lower() + random.choice(self.name['descriptiveName'])
    
    
    def get_wrong_variable_name(self):
        if random.random() < 0.25:
            return random.choice(self.name['name']).upper()
        elif random.random() < 0.25:
            return random.choice(self.name['verb'])
        else:
            return random.choice(self.name['reservedWords']).lower()
    
    
    def get_correct_method_name(self):
        if random.random() < 0.25:
            return random.choice(self.name['verb']).lower()
        if random.random() < 0.25:
            return random.choice(self.name['verb']).lower() + random.choice(self.name['adjective'])
        if random.random() < 0.25:
            return random.choice(self.name['verb']).lower() + random.choice(self.name['name'])
        else:
            return random.choice(self.name['verb']).lower() + random.choice(self.name['descriptiveName'])
    
    
    def get_wrong_method_name(self):
        if random.random() < 0.25:
            return random.choice(self.name['verb']).lower()
        if random.random() < 0.25:
            return random.choice(self.name['verb']).lower() + random.choice(self.name['adjective']).lower()
        if random.random() < 0.25:
            return random.choice(self.name['verb']).lower() + random.choice(self.name['name']).lower()
        else:
            return random.choice(self.name['verb']).lower() + random.choice(self.name['descriptiveName']).lower()

    def generateClass(self):
        if random.random() < 0.5:
            return [self.get_correct_class_name(),True]
        else:
            return [self.get_wrong_class_name(),False]
    def generateVariable(self):
        if random.random() < 0.5:
            return [self.get_correct_variable_name(),True]
        else:
            return [self.get_wrong_variable_name(),False]
    def generateMethod(self):
        if random.random() < 0.5:
            return [self.get_correct_method_name(),True]
        else:
            return [self.get_wrong_method_name(),False]
  
    def generate(self):
        X                = {} 
        X['method']      = self.generateMethod()
        X['variable']    = self.generateVariable()
        X['class']       = self.generateClass()
        ANSWER           = [X[i][1] for i in X]
        if True not in ANSWER: ANSWER.append(True)  
        else : ANSWER.append(False)
        
        QUESTION    = self.template.format(**X)  
        CHOICES     = self.choice
        print(QUESTION)
        for i in self.choice: print(i)
        print("\nanswer: ", ANSWER)
            
        return  [QUESTION ,CHOICES , ANSWER]
    

if __name__=="__main__":
    
    name = NamingConvention()
    question = name.generate()



