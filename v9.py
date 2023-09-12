# v9.py
# 年金原簿honnin_v7のもとでの検証

import dummy
dummy.honnin='honnin_v7'
dummy.definitions='definitions_simple'

from essentials import *
from f7 import 被保険者
from f9 import 被保険者資格喪失
d=Int('d')

t1=Solver()
t2=Solver()
p1=ForAll(d,Implies(成立に至る(NOT(被保険者))(d),被保険者資格喪失(d)))
p2=ForAll(d,Implies(被保険者資格喪失(d),成立に至る(NOT(被保険者))(d)))
t1.add(p1)
t2.add(p2)
print(t1.check()) # sat
print(t2.check()) # unsat
