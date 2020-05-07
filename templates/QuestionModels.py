import os
import random, json

class QuestionModel:
    TYPE = None
    DIFFICULTY_LEVEL = None
    KEYWORDs = None
    QUESTION = None
        

    def generate(self, n=1, Print=True):
        pass

    def model(self):
        X = {}

        return X


class MultipleChoice(QuestionModel):
    CHOICES = ["{choice[0]}",
               "{choice[1]}",
               "{choice[2]}",
               "{choice[3]}"]
    ANSWER  = '{answer}'
    shuffle = True
    def isShuffle(self):
        return self.shuffle
    
    def generate(self, Print=True):
        X = self.model()
        if self.isShuffle():
            random.shuffle(self.CHOICES)
        if Print:
            print('< - - - - - - - - - - >')
            print(self.QUESTION.format(**X))
            print('\n')
            for choice in self.CHOICES:
                print(". ", choice.format(**X))
            print("\n ANSWER: " , self.ANSWER.format(**X))
            print('< - - - - - - - - - - >')

        return {
            "QUESTION"  : self.QUESTION.format(**X),
            "CHOICES"   : [choice.format(**X) for choice in self.CHOICES],
            "ANSWER"    : self.ANSWER.format(**X)
                }



class NamingConvention(MultipleChoice):
    def __init__(self):
        BASE_DIR    = os.path.dirname(os.path.dirname(__file__))
        DIR         = os.path.join(BASE_DIR,'data','javanameconvention.json')
        with open(DIR) as f:
            self.name = json.load(f)
            
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