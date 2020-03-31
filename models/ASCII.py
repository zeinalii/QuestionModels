


import random
import string

class ASCII:
    def __init__(self):
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
        self.QUESTION   = "Note that the ASCII value for character {character} is {ASCII}. \
What does the expression \"{character}\" + 1 evaluate to?"
        
    def generate(self):
        X       = {}
        
        X['character']  = random.choice(string.ascii_uppercase)
        X['ASCII']      = ord(X['character'])
        X['choice']     = [ X['ASCII'] + 1,
                            chr(X['ASCII'] + 1),
                            X['character'] + '1',
                            "Syntax error (illegal expression)"]
        self.ANSWER     = X['character'] + '1'
        print('\n')
        print(self.QUESTION.format(**X))
        for i in self.CHOICES: 
            print(". ",i.format(**X))
        print("\nAnswer: ", self.ANSWER.format(**X))
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]

 


if __name__ == "__main__":
    
    ascII = ASCII()
    for i in range(10):
        _ = ascII.generate()

