



import random

class VariableType:
    def __init__(self):
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}"]
        self.QUESTION   = """If you enter {num[0]} {num[1]}, when you run this program, what will be the output?
        
        
            import java.util.Scanner;
            
            public class Test1 {{
              public static void main(String[] args) {{
                Scanner input = new Scanner(System.in);
                System.out.print("Enter three numbers: ");
                int num1 = input.nextDouble();
                int num2 = input.nextDouble();
            
                // Compute average
                double average = {expression};
            
                // Display result
                System.out.println(average);
              }}
            }}        
        """
        
    def generate(self):
        X               = {}
        expression      = []
        a        = int(random.random() * 100) / 10
        b        = int(random.random() * 100) / 10
        X['num'] = [a , b]
        expression.append('(int) (num1 + num2) / 2')
        expression.append('((int) num1 + num2)/2')
        expression.append('((int) num1 + (int) num2)/2')
        expression.append('(num1 + num2) / 2')
        choices = [float(int(a + b) / 2),
                         float((int(a)+b)/2),
                         float((int(a)+int(b))//2),
                         float((a+b)/2)]
        # choosing an expression from one the 4 availble options
        i = random.randint(0,3)
        X['expression'] = expression[i]
        ANSWER          = choices[i]
        # adding one more option if there wasn't 4 unique options
        if len(set(choices)) == 4:
            X['choice'] = choices
        elif len(set(choices)) == 3:
            X['choice'] = list(set(choices))
            X['choice'].append(int(ANSWER))
        else:
            return self.generate()

        print('\n')
        print(self.QUESTION.format(**X))
        for i in self.CHOICES: 
            print(". ",i.format(**X))
        print("\nAnswer: ", ANSWER)
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                ANSWER]
        

 


if __name__ == "__main__":
    
    variabletype = VariableType()
    for i in range(20):
        _ = variabletype.generate()



