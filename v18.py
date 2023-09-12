# v18.py

import dummy
dummy.definitions='definitions_simple'
dummy.honnin='honnin_v18'

from essentials import *
from f18 import * #第十八条年金の支給期間及び支払期月
m1=Int('m1')
m2=Int('m2')
s=Solver()
t=Solver()
r=Solver()
t.add(停止(10500/30+1))
print('10500/30+1','停止',t.check())
# 10500/30+1 停止 unsat
# 停止せず、月10500/30には停止事由発生と消滅が共に起きるから。

r.add(停止(12500/30+1))
print('12500/30+1','停止',r.check())
# 12500/30+1 停止 sat

s.add(支給(m1))
s.add(停止(m2))
s.push()
s.add(m1==m2)
print('支給と停止が同じ月に起きるか？',s.check())
# unsat　

s.pop()
s.add(m1==m2+1)
print('停止の翌月に支給されることがあるか？',s.check())
print (s.model())
# 停止の翌月に支給されることがあるか？
# sat
# [m2 = 433,
#  m1 = 434,
#  d1!10 = 12500,
#  d1!9 = 10000,
#  d2!8 = [else -> 13000]]

a=Int('a')
r.add(年金支払額(440)==a)
print('月440の支払額は？',r.check())
print('a=',r.model()[a])

# sat
# a=140000
