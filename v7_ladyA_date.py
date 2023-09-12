# v7_ladyA_date.py
# 第七条の検証で使用
# 年金原簿honnin_ladyA_dateに関する検証

import dummy
dummy.honnin='honnin_ladyA_date'
dummy.definitions='definitions_date_3'

from essentials import *
from f7 import *
d=Int('d')

import time
start=time.time()

## 同じ日には異なる種別の被保険者にはなれないことの確認 ##

s=Solver()
p=Or(And(第一号被保険者(d),第二号被保険者(d)),
     And(第一号被保険者(d),第三号被保険者(d)),
     And(第二号被保険者(d),第三号被保険者(d)))
s.add(p)
print(s.check())
print(time.time()-start,'sec')
# unsat
