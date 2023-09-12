# defintions_abs
from essentials import *

Day,(d1,d2,d3,d4,d5,d6)= \
        EnumSort('Day',('d1','d2','d3','d4','d5','d6'))
p=Function('p',Day,Day,BoolSort())
x,y,z=Consts('x y z',Day)
orderDay=And(
  ForAll(x,p(x,x)),
  ForAll([x,y,z],Implies(And(p(x,y),p(y,z)),p(x,z))),
  ForAll([x,y],Implies(And(p(x,y),p(y,x)),x==y)),
  ForAll([x,y],Or(p(x,y),p(y,x))))
between=(lambda x,y,z:And(p(x,y),p(y,z)))

# Month,(m1,m2,m3,m4,m5,m6,m7)= \
#         EnumSort('Month',('m1','m2','m3','m4','m5','m6','m7'))
# x,y,z=Consts('x y z',Month)
# q=Function('q',Month,Month,BoolSort())
# orderMonth=And(
#   ForAll(x,q(x,x)),
#   ForAll([x,y,z],
#     Implies(And(q(x,y),q(y,z)),q(x,z))),
#   ForAll([x,y],
#     Implies(And(q(x,y),q(y,x)),x==y)),
#   ForAll([x,y],Or(q(x,y),q(y,x))))
#
# 属月=(lambda d:
#         If(d==d1,m1,If(d==d2,m3,If(d==d3,m4,If(d==d4,m6,m7)))))
# 次月=(lambda m:
#         If(m==m1,m2,If(m==m2,m3,If(m==m3,m4,If(m==m4,m5,If(m==m5,m6,m7))))))
