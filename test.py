
from QuestionModels.MultipleChoiceStringManipulation import MultipleChoiceStringManipulation
from QuestionModels.MathExpression import MathExpression
from QuestionModels.booleanMultipleChoice import booleanMultipleChoice
from QuestionModels.booleanMultipleChoice2 import booleanMultipleChoice2
from QuestionModels.booleanMultipleChoice3 import booleanMultipleChoice3
from QuestionModels.ASCII import ASCII
from QuestionModels.FloatInteger import FloatInteger
from QuestionModels.NamingConvention import NamingConvention
from QuestionModels.StringManipulationShortAnswer import StringManipulationShortAnswer


if __name__=="__main__":
    # 1- substring
    model = MultipleChoiceStringManipulation()
    [QUESTION, CHOICES, ANSWER] = model.generateSubstringQuestion()
    # 2- indexOf
    model = MultipleChoiceStringManipulation()
    [QUESTION, CHOICES, ANSWER] = model.generateIndexOfQuestion()    
    # 3- MathExpression
    model = MathExpression()
    [QUESTION, CHOICES, ANSWER] = model.generate()    
     # 4- booleanMultipleChoice
    model = booleanMultipleChoice()
    [QUESTION, CHOICES, ANSWER] = model.generate()   
     # 5- booleanMultipleChoice2
    model = booleanMultipleChoice2()
    [QUESTION, CHOICES, ANSWER] = model.generate()   
     # 6- booleanMultipleChoice2
    model = booleanMultipleChoice3()
    [QUESTION, CHOICES, ANSWER] = model.generate()   
     # 7- NamingConvention
    model = NamingConvention()
    [QUESTION, CHOICES, ANSWER] = model.generate() 
     # 8- FloatInteger
    model = FloatInteger()
    [QUESTION, CHOICES, ANSWER] = model.generate()  
    

     # short answer - String Manipulation
    model = StringManipulationShortAnswer()
    [QUESTION, ANSWER] = model.generate()  





              