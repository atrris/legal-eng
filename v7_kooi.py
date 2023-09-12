
import dummy
dummy.honnin='honnin_v7'
from essentials import * # honnin_v7
from f7 import *
d=Int('d')
d=200
print(第一号被保険者(d))






#
# # 日450は，第号被保険者か？
# unsat
#
s=Solver()
s.add(第一号被保険者(200))
print(s.check())
# sat
#
# s=Solver()
# s.add(第三号被保険者(450))
# print(s.check())
# # unsat
#
# # 日450以外に第二号被保険者になりえるか？
# t=Solver()
# t.add(第二号被保険者(d),d!=450)
# if t.check()==sat:
#     print(t.model())
# # [d=368]
#
# # 同時に異なる種別の被験者になり得るか？
# s=Solver()
# p=Or(And(第一号被保険者(d),第二号被保険者(d)),
#      And(第一号被保険者(d),第三号被保険者(d)),
#      And(第二号被保険者(d),第三号被保険者(d)))
# s.add(p)
# print(s.check())
# # unsat
#
# # honnin_v7においては，第一号，第二号，第三号被保険者である日は，それぞれ
# # 第一号被保険者：日201〜日300 および 日550〜日599
# # 第二号被保険者：日301〜日499
# # 第三号被保険者：日500〜日549
# # であるが，これは以下のようであるが，これは次のようにして確認できる．
#
# t=Solver()
# p1 = ForAll(d,第一号被保険者(d)==Or(And(201<=d,d<=300),And(550<=d,d<=599)))
# p2 = ForAll(d,第二号被保険者(d)==And(301<=d,d<=499))
# p3 = ForAll(d,第三号被保険者(d)==And(500<=d,d<=549))
# t.add(p1,p2,p3)
# print(t.check())
# # sat
