from PYfoodapi import *


food = foodapi()
data = food.makequery("1kg steak")
print(data)
