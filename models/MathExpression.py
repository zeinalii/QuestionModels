


import random

class MathExpression:
    def __init__(self):
        self.CHOICES    = [ "{choice[0]}",
                            "{choice[1]}",
                            "{choice[2]}",
                            "{choice[3]}",
                            "{choice[4]}"]
        self.QUESTION   = "The expression {expression} is evaluated to"
        self.ANSWER   = "{answer}"
        
    def generate(self):
        X = self.GenerateQuestion()
        """replace X inside the Qestion and Choices and then print them """
        print('\n')
        print(self.QUESTION.format(**X))
        for i in self.CHOICES: 
            print(". ",i.format(**X))
        print("\nAnswer: ", self.ANSWER.format(**X))
        return [self.QUESTION.format(**X), 
                [CHOICE.format(**X) for CHOICE in self.CHOICES],
                self.ANSWER.format(**X)]

    def GenerateQuestion(self):   
        X = {}
        X['x'] = random.sample([i for i in range(1,21)],4)
        random.shuffle(X['x'])
        X['o'] = random.sample(['//','-','*'],k=3)
        X['o'].append(random.choice(['+','//','-','*']))
        bracket = "({x[2]} {o[3]} {x[3]})".format(**X)
        X['x'][3] = bracket
        random.shuffle( X['x'])
        expression = "{x[0]} {o[0]} {x[1]} {o[1]} {x[2]} {o[2]} {x[3]}".format(**X)
        try:
            X['expression'] = expression.replace('//','/')
            X['answer'] = eval(expression)
            choice = [expression]
            choice.append("({x[0]} {o[0]} ({x[1]} {o[1]} {x[2]})) {o[2]} {x[3]}".format(**X))
            choice.append("(({x[0]} {o[0]} {x[1]}) {o[1]} {x[2]}) {o[2]} {x[3]}".format(**X))
            choice.append("{x[0]} {o[0]} (({x[1]} {o[1]} {x[2]}) {o[2]} {x[3]})".format(**X))
            choice.append("{x[0]} {o[0]} ({x[1]} {o[1]} ({x[2]} {o[2]} {x[3]}))".format(**X))
            choice.append("(({x[0]} {o[0]} {x[1]}) {o[1]} ({x[2]} {o[2]} {x[3]}))".format(**X))
            for i in range(6):
                choice.append('int(' + choice[i].replace('//','/') + ')')
            choice = [eval(i) for i in choice]
            if len(set(choice)) > 4:
                X['choice'] = random.sample(set(choice),5)
                if X['answer'] not in X['choice']:
                    X['choice'][0] = X['answer']
            else:
                X = self.GenerateQuestion()
        except:
             X = self.GenerateQuestion()
        return X


if __name__ == "__main__":
    
    mathexpression = MathExpression()
    for i in range(10):
        _ = mathexpression.generate()
    """
    Result:
        The expression 1 - 5 / 11 * (11 + 4) is evaluated to
        .  -1
        .  1
        .  15
        .  -15
        .  8
        
        Answer:  1
    """
