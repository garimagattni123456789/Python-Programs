import module1
module1.square(4)
print(module1.pi)

module1.login("garima","garima")

#second way
import module1 as m
m.square(133)
print(m.pi)
m.login("garima","garima")
m.login("garima","gattani")

import module1 as a
a.square(152)
print(a.pi)
a.login("aaaaaa","jjjjjj")
a.login("python","python")

#third way
from module1 import pi,square,login
print(pi)
square(4)
login("aaa","aaa")

#forth way
from module1 import*
square(4)
login("abc","abc")
print(pi)
