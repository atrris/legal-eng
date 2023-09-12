# v18_abs.py
import dummy
dummy.definitions='definitions_v18_abs'
dummy.honnin='honnin_v18_abs'

#from essentials import *
from f18 import *
d1,d2=Consts('d1 d2',Day)
m,m1,m2=Consts('m m1 m2',Month)
s=Solver()
s.add(orderMonth,orderDay,seqMonth,seqDay)
s.push()

# 支給事由が発生した月は支給されず，次月から支給が開始され，停止事由が成立する月まで
# 支給される．
prop1=ForAll([d1,d2,m1,m2,m],
        Implies(And(支給事由発生(d1),停止事由発生(d2),m1==属月(d1),m2==属月(d2)),
                And(Not(支給(m1)),
                    Implies(And(q(次月(m1),m),q(m,m2)),
                            And(支給(m))))))
s.add(prop1)
print(s.check())
# sat
print(s.model())
# [p = [else ->
#       Or(And(Var(0) == D4, Var(1) == D4),
#          And(Var(0) == D3, Var(1) == D3),
#          And(Var(0) == D1, Var(1) == D1),
#          And(Var(0) == D2, Var(1) == D2),
#          And(Var(0) == D3, Var(1) == D4),
#          And(Var(0) == D1, Var(1) == D3),
#          And(Var(0) == D1, Var(1) == D2),
#          And(Var(0) == D2, Var(1) == D3),
#          And(Var(0) == D1, Var(1) == D4),
#          And(Var(0) == D2, Var(1) == D4))],
#  q = [else ->
#       Or(And(Var(0) == M3, Var(1) == M3),
#          And(Var(0) == M2, Var(1) == M2),
#          And(Var(0) == M1, Var(1) == M3),
#          And(Var(0) == M223, Var(1) == M223),
#          And(Var(0) == M11, Var(1) == M4),
#          And(Var(0) == M112, Var(1) == M4),
#          And(Var(0) == M2, Var(1) == M33),
#          And(Var(0) == M2, Var(1) == M22),
#          And(Var(0) == M1, Var(1) == M4),
#          And(Var(0) == M22, Var(1) == M22),
#          And(Var(0) == M3, Var(1) == M33),
#          And(Var(0) == M11, Var(1) == M334),
#          And(Var(0) == M334, Var(1) == M334),
#          And(Var(0) == M223, Var(1) == M33),
#          And(Var(0) == M11, Var(1) == M11),
#          And(Var(0) == M22, Var(1) == M334),
#          And(Var(0) == M223, Var(1) == M4),
#          And(Var(0) == M112, Var(1) == M223),
#          And(Var(0) == M1, Var(1) == M33),
#          And(Var(0) == M11, Var(1) == M22),
#          And(Var(0) == M112, Var(1) == M112),
#          And(Var(0) == M1, Var(1) == M1),
#          And(Var(0) == M223, Var(1) == M334),
#          And(Var(0) == M22, Var(1) == M33),
#          And(Var(0) == M22, Var(1) == M4),
#          And(Var(0) == M2, Var(1) == M223),
#          And(Var(0) == M334, Var(1) == M4),
#          And(Var(0) == M1, Var(1) == M2),
#          And(Var(0) == M11, Var(1) == M33),
#          And(Var(0) == M22, Var(1) == MM),
#          And(Var(0) == M33, Var(1) == M334),
#          And(Var(0) == M3, Var(1) == M334),
#          And(Var(0) == M112, Var(1) == M3),
#          And(Var(0) == M1, Var(1) == M11),
#          And(Var(0) == M2, Var(1) == M3),
#          And(Var(0) == M112, Var(1) == M22),
#          And(Var(0) == M11, Var(1) == M112),
#          And(Var(0) == M33, Var(1) == M4),
#          And(Var(0) == M4, Var(1) == M4),
#          And(Var(0) == M2, Var(1) == M4),
#          And(Var(0) == M1, Var(1) == M22),
#          And(Var(0) == M112, Var(1) == M334),
#          And(Var(0) == M112, Var(1) == M2),
#          And(Var(0) == M33, Var(1) == M33),
#          And(Var(0) == M1, Var(1) == M112),
#          And(Var(0) == M1, Var(1) == M334),
#          And(Var(0) == M3, Var(1) == M4),
#          And(Var(0) == M223, Var(1) == M3),
#          And(Var(0) == M1, Var(1) == M223),
#          And(Var(0) == MM, Var(1) == M33),
#          And(Var(0) == M11, Var(1) == M223),
#          And(Var(0) == M2, Var(1) == MM),
#          And(Var(0) == M2, Var(1) == M334),
#          And(Var(0) == M11, Var(1) == M2),
#          And(Var(0) == MM, Var(1) == MM),
#          And(Var(0) == M112, Var(1) == M33),
#          And(Var(0) == M11, Var(1) == M3),
#          And(Var(0) == M22, Var(1) == M3),
#          And(Var(0) == M22, Var(1) == M223),
#          And(Var(0) == MM, Var(1) == M3),
#          And(Var(0) == MM, Var(1) == M334),
#          And(Var(0) == M1, Var(1) == MM),
#          And(Var(0) == MM, Var(1) == M223),
#          And(Var(0) == M112, Var(1) == MM),
#          And(Var(0) == M11, Var(1) == MM),
#          And(Var(0) == MM, Var(1) == M4))]]

s.pop()
s.push()

# 停止事由が発生した月の次月から停止事由が消滅する月まで支給は停止する．
prop2=ForAll([d1,d2,m1,m2,m],
        Implies(And(停止事由発生(d1),停止事由消滅(d2),m1==属月(d1),m2==属月(d2)),
                And(Not(停止(m1)),
                    Implies(And(q(次月(m1),m),q(m,m2)),
                            And(停止(m))))))
s.add(prop2)
print(s.check())
# sat

s.pop()
s.push()

# 停止事由が成立する月の次月から受給権が消滅する月まで支給される．
prop3=ForAll([d1,d2,m1,m2,m],
        Implies(And(停止事由消滅(d1),受給権利消滅(d2),m1==属月(d1),m2==属月(d2)),
                And(Not(支給(m1)),
                    Implies(And(q(次月(m1),m),q(m,m2)),
                            And(支給(m))))))
s.add(prop3)
print(s.check())
# sat

s.pop()
s.push()

# 支給と停止が共に成立する月はない．
prop4=And(支給(m),停止(m))
s.add(prop4)
print(s.check())
# unsat
