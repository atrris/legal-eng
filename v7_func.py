# v7_func
# 第七条の検証
# 同時に異なる種別の被保険者にはなれないことを，v7の場合のように具体的な
# 年金原簿に対してではなく，より一般的に検証する．
# "日本国内に住所を有する”などを述語変数として扱い，これににいかなる述語を代入
# しても充足出来ないことを示す．

import dummy
dummy.honnin='honnin_v7_func'
from essentials import * 
from f7 import *
d=Int('d')
s=Solver()
p=Or(And(第一号被保険者(d),第二号被保険者(d)),
     And(第一号被保険者(d),第三号被保険者(d)),
     And(第二号被保険者(d),第三号被保険者(d)))
s.add(p)
print(s.check())
# unsat
