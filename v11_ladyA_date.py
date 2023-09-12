# v11_ladyA_date
# 年金原簿　honnin_ladyA_dateのもとでの検証
import dummy
dummy.honnin='honnin_ladyA_date'
dummy.definitions='definitions_date_3'
from essentials import *
from f11 import * # 第十一条被保険者期間の計算
import time
m=Int('m')

start=time.time()
L1=充足リスト(第一号被保険者期間,500)
L1=[mjm2ym(mjm) for mjm in L1]
print("第一号被保険者期間",'\n',L1)
print(len(L1)) #134
print(time.time()-start,'sec','\n')
# 0.460216760635376 sec

start=time.time()
L2=充足リスト(第二号被保険者期間,500)
L2=[mjm2ym(mjm) for mjm in L2]
print("第二号被保険者期間",'\n',L2)
print(len(L2)) #318
print(time.time()-start,'sec','\n')
# 0.6563467979431152 sec

start=time.time()
L3=充足リスト(第三号被保険者期間,500)
L3=[mjm2ym(mjm) for mjm in L3]
print("第三号被保険者期間",'\n',L3)
print(len(L3)) #28
print(time.time()-start,'sec','\n')
# 0.2897191047668457 sec

# ある月が同時に複数の異なる被保険者期間に属することはないことの検証
start=time.time()
m=Int('m')
s=Solver()
s.add(Or(And(第一号被保険者期間(m),第二号被保険者期間(m)),
         And(第一号被保険者期間(m),第三号被保険者期間(m)),
         And(第二号被保険者期間(m),第三号被保険者期間(m))))
print(s.check(),'\n','異なる被保険者期間に属する月は無い')
print(time.time()-start,'sec')
# unsat
# 1.5195868015289307 sec
