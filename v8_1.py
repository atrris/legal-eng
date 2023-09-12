# v8_1.py
# 年金原簿honnin_v7に関してf8_1が正しいことの検証

import dummy
dummy.honnin='honnin_v7'
dummy.definitions='definitions_simple'

import f8_1,f7
from essentials import *
d=Int('d')

p=ForAll(d,f8_1.被保険者資格取得(d)==成立に至る(f7.被保険者)(d))
t=Solver()
t.add(p)
print(t.check()) # sat
