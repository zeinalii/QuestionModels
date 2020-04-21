


import random
import string

class Remainder:
    def __init__(self):
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}",
                            "{choice[4]}"]
        self.QUESTION   = "Which of the following values results in {value}?"
        
    def generate(self):
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
        i          = random.choice(range(len(results)))
        X['value'] = results[i]
        ANSWER     = X['choice'][i]
        print('\n')
        print(self.QUESTION.format(**X))
        for i in self.CHOICES: 
            print(". ",i.format(**X))
        print("\nAnswer: ", ANSWER)
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                ANSWER]
        

 


if __name__ == "__main__":
    
    remainder = Remainder()
    for i in range(10):
        _ = remainder.generate()



