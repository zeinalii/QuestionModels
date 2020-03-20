import random
import json

"""
public class MyClass {
  static double getArea() {
    double Pi_Number = 3.14159;
    double radius = 5;
    return Pi_Number * radius * radius;
  }

  public static void main(String[] args) {
    System.out.println(getArea());
  }
}
"""


class Name:
    def __init__(self, name):
        self.name = name
            
    # < --------------------- >
    def get_correct_class_name(self):
        return random.choice(self.name['name'])
    
    
    def get_wrong_class_name(self):
        if random.random() < 0.3:
            return random.choice(self.name['name']).lower()
        elif random.random() < 0.3:
            return random.choice(self.name['name']).upper()
        elif random.random() < 0.3:
            return random.choice(self.name['adjective']).lower()
        elif random.random() < 0.3:
            return random.choice(self.name['reservedWords']).lower()
        else:
            return random.choice(self.name['verb'])
    
        # < --------------------- >
    
    
    def get_correct_variable_name(self):
        if random.random() < 0.3:
            return random.choice(self.name['descriptiveName']).lower()
        else:
            return random.choice(self.name['name']).lower() + random.choice(self.name['descriptiveName'])
    
    
    def get_wrong_variable_name(self):
        if random.random() < 0.3:
            return random.choice(self.name['name']).upper()
        elif random.random() < 0.3:
            return random.choice(self.name['verb'])
        elif random.random() < 0.3:
            return random.choice(self.name['reservedWords']).lower()

        # < --------------------- >
    
    
    def get_correct_method_name(self):
        if random.random() < 0.3:
            return random.choice(self.name['verb']).lower()
        if random.random() < 0.3:
            return random.choice(self.name['verb']).lower() + random.choice(self.name['adjective'])
        if random.random() < 0.3:
            return random.choice(self.name['verb']).lower() + random.choice(self.name['name'])
        else:
            return random.choice(self.name['verb']).lower() + random.choice(self.name['descriptiveName'])
    
    
    def get_wrong_method_name(self):
        if random.random() < 0.3:
            return random.choice(self.name['verb']).lower()
        if random.random() < 0.3:
            return random.choice(self.name['verb']).lower() + random.choice(self.name['adjective']).lower()
        if random.random() < 0.3:
            return random.choice(self.name['verb']).lower() + random.choice(self.name['name']).lower()
        else:
            return random.choice(self.name['verb']).lower() + random.choice(self.name['descriptiveName']).lower()


if __name__=="__main__":
    
    with open('javanameconvention.json') as f:
        name = json.load(f)
    name = Name(name)
    print(name.get_correct_class_name())
    print(name.get_correct_variable_name())
    print(name.get_correct_method_name())
    print(name.get_wrong_class_name())
    print(name.get_wrong_variable_name())
    print(name.get_wrong_method_name())
    
    