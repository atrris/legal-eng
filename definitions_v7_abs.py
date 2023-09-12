# defintions_v7_abs.py
from essentials import *

Day,(D1,D2,D3,D4,D5,D6)= \
        EnumSort('Day',('D1','D2','D3','D4','D5','D6'))
p=Function('p',Day,Day,BoolSort())
x,y,z=Consts('x y z',Day)
orderDay=And(
        ForAll(x,p(x,x)),
        ForAll([x,y,z],Implies(And(p(x,y),p(y,z)),p(x,z))),
        ForAll([x,y],Implies(And(p(x,y),p(y,x)),x==y)),
        ForAll([x,y],Or(p(x,y),p(y,x))))
between=(lambda x,z:lambda y:And(p(x,y),p(y,z)))
