# v11 第十一条の検証
# 年金原簿honnin_v7のもとでの検証
import dummy
dummy.honnin='honnin_v7'
dummy.definitions='definitions_simple'

from f11 import *
import time
start=time.time()
d=Int('d')
solve(被保険者資格取得(d)) # d=200
solve(被保険者資格喪失(d)) # d=601
L1=充足リスト(第一号被保険者期間,30)
L2=充足リスト(第二号被保険者期間,30)
L3=充足リスト(第三号被保険者期間,30)
L=充足リスト(被保険者期間,30)
print("被保険者期間",L)
# [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print("第一号被保険者期間",L1)
# [6, 7, 8, 9, 18, 19]
print("第二号被保険者期間",L2)
# [10, 11, 12, 13, 14, 15]
print("第三号被保険者期間",L3)
# [16, 17]

# ある月が同時に複数の異なる被保険者期間に属することはないことの検証
m=Int('m')
s=Solver()
s.add(Or(And(第一号被保険者期間(m),第二号被保険者期間(m)),
         And(第一号被保険者期間(m),第三号被保険者期間(m)),
         And(第二号被保険者期間(m),第三号被保険者期間(m))))
print(s.check())
# unsat
print(time.time()-start,'sec')
# 1.5498101711273193 sec
