# v94.py　
# 第九十四条保険料の追納の年金原簿honnin_ladyA_dateのもとでのテスト

import dummy
dummy.honnin='honnin_ladyA_date'
dummy.honnin_post='honnin_ladyA_post'
dummy.definitions='definitions_date_3'

import time
start=time.time()
from essentials import * # honnin_ladyA
from f94 import *
m,m1=Ints('m m1')
e=Const('e',保険料免除種別)

s=Solver()
s.add(追納可能(通月(1980,10),m,学生))
print(s.check()) # sat
print(YM(s.model()[m].as_long())) # (1975.0, 4)
# (1975,4)はhonnin_ladyA_dateにおいて，保険料免除_学生がTrueとなる最初の月

u=Solver()
u.add(ForAll([m,m1,e],Implies(追納可能(m,m1,e),And(P,Q,R))))
print(u.check())
# sat  本人,本人_postはP,Q,Rを満たしている．

# 追納申請日を変えると結果は異なる．
r=Solver()
r.add(追納可能(通月(2010,1),m,学生))
print(r.check())
# unsat　西暦2010年1月以降では，保険料免除_学生はない．

t=Solver()
t.add(追納可能(通月(2010,1),m,半額))
print(t.check()) # sat
print(YM(t.model()[m].as_long())) # (2007.0, 2)
# (2007,2)は半額免除となる最初の月

print(time.time()-start,'sec')
# 0.26294398307800293 sec
