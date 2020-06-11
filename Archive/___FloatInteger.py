
import random

class FloatInteger:
    def __init__(self):
        self.CHOICES    = [ "( int )( {value[0]:7.4f} * {value[1]} ) / {value[1]}",
                            "( int )( {value[0]:7.4f} * {value[1]} ) / {value[1]}.0",
                            "( int )( {value[0]:7.4f} * {value[1]} / {value[1]} )",
                            "( int )( {value[0]:7.4f} ) * {value[1]} / {value[1]}.0"]
        self.QUESTION   = "Which of the following expression results in {question}?"
        self.ANSWER     = self.CHOICES[1]
    def generate(self):
        X           = {}
        X['value']  = [random.random()*100,            # generating a random number between 0 and 100
                         random.choice([10,100,1000])] # choosing values between 10,100,1000
        
        X['question'] = int(X['value'][0]*X['value'][1])/X['value'][1]
        print('\n')
        print(self.QUESTION.format(**X))
        for i in self.CHOICES: 
            print(". ",i.format(**X))
        print("\n--> answer: ", self.ANSWER.format(**X))
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]
if __name__ == "__main__":
    
    floatinteger = FloatInteger()
    _ = floatinteger.generate()
