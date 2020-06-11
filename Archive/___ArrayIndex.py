
import random
import string

class ArrayIndex:
    def __init__(self):
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
        self.QUESTION   = """Assuming the loop body does not modify i below,\
        how many iterations will the following loop execute?
        
        for (int i = {index[0]}; i <= {index[1]}; i{counter})
        {{
        // iteration
        }}
        """
        
    def generate(self):
        X       = {}
        X['index']     = 
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


n = 0
for i in range(8,25):
    n += 1
print(n)