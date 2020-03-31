

import random

class BooleanMutipleChoice3:
    def __init__(self):
        self.CHOICES    = [ " banana",
                            " apple",
                            " apple orange",
                            " orange",
                            " apple banana",
                            " apple apple"]
        self.QUESTION   = """Suppose x = {x}, y = {y}, and z = {z}. What is the printout of the following statement? Hint: Indent the statement
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
        self.ANSWER     = '{answer}'
    def generate(self):
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
        print('\n')
        print(self.QUESTION.format(**X))
        for i in self.CHOICES: 
            print(". ",i.format(**X))
        print("\n--> answer: ", self.ANSWER.format(**X))
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]
    
if __name__ == "__main__":
    
    boolean = BooleanMutipleChoice3()
    for _ in range(10):
        _ = boolean.generate()
