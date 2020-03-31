


import random
import json




class FinalConstant:
    def __init__(self, name):
        self.name           = name
        self.CHOICES        = [ "final double {variable} = {value:2.2f}",
                               "final {variable} = {value:2.2f}",
                               "final long {variable} = {value:2.2f}",
                               "double {variable} = {value:7.2f}"]
        self.QUESTION       = """To declare a constant {variable} inside a method with value {value:2.2f}, you write:"""


    def generate(self):
        X               = {}
        X['value']      = random.random()*100
        X['variable']   = random.choice(self.name['adjective']).upper() +\
                            "_" + random.choice(self.name['descriptiveName']).upper()
        ANSWER     = self.CHOICES[0].format(**X)

        print(self.QUESTION.format(**X))
        print('\n')
        for CHOICE in self.CHOICES: print(CHOICE.format(**X))
        print('\n--> Answer: ', ANSWER)
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                ANSWER]


           
if __name__=="__main__":
    
    with open('javanameconvention.json') as f:
        name = json.load(f)
    finalconstant = FinalConstant(name)
    _ = finalconstant.generate()
