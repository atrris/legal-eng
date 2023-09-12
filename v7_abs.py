# v7_abs.py
# 抽象的日付データに基づく検証
import dummy
dummy.honnin='honnin_v7_abs'
dummy.definitions='definitions_v7_abs'

from f7 import * # 第七条被保険者の資格
d=Const('d',Day)
s=Solver()
s.add(orderDay)
# 同時に異なる種別の被保険者にはなれないことの検証
s.push()
s.add(Or(And(第一号被保険者(d),第二号被保険者(d)),
         And(第一号被保険者(d),第三号被保険者(d)),
         And(第二号被保険者(d),第三号被保険者(d))))
print(s.check())
# unsat

# 第三号被保険者になる日が存在し得ることの検証
s.pop()
s.add(第三号被保険者(d))
print(s.check())
print(s.model())

# sat
# [d = D1,
#  p = [else ->
#       Or(And(Var(0) == D6, Var(1) == D2),
#          And(Var(0) == D4, Var(1) == D4),
#          And(Var(0) == D2, Var(1) == D3),
#          And(Var(0) == D2, Var(1) == D2),
#          And(Var(0) == D4, Var(1) == D5),
#          And(Var(0) == D5, Var(1) == D5),
#          And(Var(0) == D3, Var(1) == D3),
#          And(Var(0) == D1, Var(1) == D2),
#          And(Var(0) == D4, Var(1) == D3),
#          And(Var(0) == D6, Var(1) == D6),
#          And(Var(0) == D1, Var(1) == D3),
#          And(Var(0) == D1, Var(1) == D6),
#          And(Var(0) == D6, Var(1) == D3),
#          And(Var(0) == D5, Var(1) == D1),
#          And(Var(0) == D1, Var(1) == D1),
#          And(Var(0) == D4, Var(1) == D6),
#          And(Var(0) == D5, Var(1) == D2),
#          And(Var(0) == D4, Var(1) == D1),
#          And(Var(0) == D4, Var(1) == D2),
#          And(Var(0) == D5, Var(1) == D6),
#          And(Var(0) == D5, Var(1) == D3))]]
# 抽象日データ上の全順序関係pは，p(x,y),x!=yをx<yと書くと,このモデルは
# 　　　  D4 < D5 < D1 < D6 < D2 < D3
# となっており，d=D1 とすると，
# 　　　　D5 < d < D6
# となり，第二号被保険者の配偶者の期間を満たすが，
# 　　　　D4 < d < D3
# であるので厚生年金保険の被保険者の期間を満たしておらず，
# 確かに日d=D1では，第三号被保険者であることがわかる．
# このようなモデルは唯一でない．
