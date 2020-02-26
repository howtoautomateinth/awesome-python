
class MyDecorator: 
    def __init__(self, function): 
        self.function = function 
      
    def __call__(self): 
  
        print("before the function is called.")
  
        self.function() 
  
        print("after the function is called.")
  
@MyDecorator
def function(): 
    print("Howtoautomate.in.th") 
  
if __name__ == '__main__':
    function()
