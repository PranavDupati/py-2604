# Method Overloading 

class MathOps:
    
    def add(self,a,b):
        return a + b 
    
    def add(self,a,b,c):
        return a + b + c 
    
obj = MathOps()
# obj.add(2,3)
print(obj.add(2,3,4))

# Way to achieve above 
class MathOps:
    
    def add(self,*args):
        return sum(args)

obj = MathOps()
print(obj.add(2,3))
print(obj.add(2,3,4))    