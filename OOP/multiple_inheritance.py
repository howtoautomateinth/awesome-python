class John:
    def eat(self):
        print("eat() method called")
 
class Sarah:
    def sit(self):
        print("sit() method called")
 
class David:
    def run(self):
        print("run() method called")
 
class HR(John, Sarah, David):
    def generate(self):
        print("generate() method called")
 
 
if __name__ == '__main__':
    hr = HR()
    hr.eat()
    hr.run()
    hr.sit()
    hr.generate()