# v8.py
# 年金原簿honnin_v7をテストデータとする検証

import dummy
dummy.honnin='honnin_v7'
dummy.definitions='definitions_simple'

from essentials import *
from f7 import 被保険者
from f8 import 被保険者資格取得

d=Int('d')
s=Solver()
p=ForAll(d,Implies(成立に至る(被保険者)(d),被保険者資格取得(d)))
s.add(p)
print(s.check()) # sat
t=Solver()
q=ForAll(d,Implies(被保険者資格取得(d),成立に至る(被保険者)(d)))
t.add(q)
print(t.check()) # unsat

# 実際，成立に至る(被保険者)(d)は，d=201に対してのみTrueとなるが，
# 被保険者資格取得(d)は，d=201,301,500に対してTrueとなる．
u=Solver()
u.add(成立に至る(被保険者)(d))
print(u.check()) # sat
print(u.model()) # d=201
u.add(d!=201)
print(u.check()) # unsat

v=Solver()
v.add(被保険者資格取得(d))
print(v.check()) # sat
print(v.model()) # d=301
v.add(d!=301)
print(v.check()) # sat
print(v.model()) # d=500
v.add(d!=500,d==201)
print(v.check()) # sat
print(v.model()) # d=201
