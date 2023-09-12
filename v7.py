# v7.py
# 第七条の検証
# 年金原簿honnin_v7のもとでの検証
import dummy
dummy.honnin='honnin_v7'
from essentials import *
from f7 import *
d=Int('d')

# 日450は，第何号被保険者か？
s=Solver()
s.add(第一号被保険者(450))
print(s.check())
# unsat

s=Solver()
s.add(第二号被保険者(450))
print(s.check())
# sat

s=Solver()
s.add(第三号被保険者(450))
print(s.check())
# unsat

def 被保険者の種類(d):
    s1=Solver()
    s2=Solver()
    s3=Solver()
    s1.add(第一号被保険者(d))
    s2.add(第二号被保険者(d))
    s3.add(第三号被保険者(d))
    if s1.check()==sat: return '第一号被保険者'
    elif s2.check()==sat: return '第二号被保険者'
    elif s3.check()==sat: return '第三号被保険者'

print(被保険者の種類(450)) #第二号被保険者

# 日450以外に第二号被保険者になりえるか？
t=Solver()
t.add(第二号被保険者(d),d!=450)
if t.check()==sat:
    print(t.model())
# [d=368]

# 同時に異なる種別の被験者になり得るか？
s=Solver()
p=Or(And(第一号被保険者(d),第二号被保険者(d)),
     And(第一号被保険者(d),第三号被保険者(d)),
     And(第二号被保険者(d),第三号被保険者(d)))
s.add(p)
print(s.check())
# unsat

# honnin_v7においては，第一号，第二号，第三号被保険者である日は，それぞれ
# 第一号被保険者：日201〜日300 および 日550〜日599
# 第二号被保険者：日301〜日499
# 第三号被保険者：日500〜日549
# であるが，これは以下のようであるが，これは次のようにして確認できる．

t=Solver()
p1 = ForAll(d,第一号被保険者(d)==Or(And(201<=d,d<=300),And(550<=d,d<=599)))
p2 = ForAll(d,第二号被保険者(d)==And(301<=d,d<=499))
p3 = ForAll(d,第三号被保険者(d)==And(500<=d,d<=549))
t.add(p1,p2,p3)
print(t.check())
# sat
