# Inbuilt Modules

# 1st Syntax 
# print(math.pi) # NameError: name 'math' is not defined. Did you forget to import 'math'?
import math
print(math.pi)
print(math.sqrt(25))

# 2nd Syntax - recommended
from math import pi,sqrt
print(pi)
print(sqrt(25))

