
import random




"""
public class MyClass {
  static void myMethod() {
    System.out.println("I just got executed!");
  }

  public static void main(String[] args) {
    myMethod();
  }
}
"""







def getVerb():
    verb = ['find',
            'get',
            'send',
            'print',
            'compare',
            'remove',
            'delete',
            'copy',
            'clone']
    return random.choice(verb)
            
def getDescriptiveName():
    DescriptiveName = ['area',
            'angle',
            'size',
            'length',
            'age',
            'point',
            'name',
            'id',
            'speed ']
    return random.choice(DescriptiveName)

def getName():
    name = ["Car",
            "Bird",
            "Plane",
            "Board",
            "Player",
            "Animal"]
    return random.choice(name)

def getAdjective():
    adjective = ["max",
                 "min",
                 "midle",
                 "final",
                 "fist",
                 "last"]
    return random.choice(adjective)

def getReservedWords():
    ReservedWords = ["class",
             "for",
             "implement",
             "while",
             "goto",
             "end",
             "else"
            ]
    return random.choice(ReservedWords)

def getVariableName():
    DescriptiveName = getDescriptiveName()
    return (getAdjective() + 
            DescriptiveName[0].capitalize() + 
            DescriptiveName[1:])
    
def getWrongVariableName():
    if random.random() < 0.3:
        return getReservedWords()
    elif random.random() < 0.3:
        return getVariableName().lower()
    
    
    
    
    
    
    
    
    
    
    

 