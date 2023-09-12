# fH16_104_19.py　附則（平成一六年六月一一日法律第一〇四号）第十九条　若年納付猶予の検証
# 年金原簿honnin_ladyB_H16_104_19のもとで，保険料納付猶予_若年1を満たす月を確認
# 配偶者の年金原簿は，本人のもので代用した．

import dummy
dummy.honnin='honnin_ladyB_H16_104_19' # 本人
dummy.haiguusha='honnin_ladyB_H16_104_19' # 配偶者：本人で代用
dummy.definitions='definitions_date_3'

import time
start=time.time()
from essentials import *
from fH16_104_19 import *
y,m,m1=Ints('y m m1')

s=Solver()
s.add(保険料納付猶予_若年1(m))
print(s.check())
print(s.model()) # [m = 1757]
solve(s.model()[m]==通月(平成(y),m1),1<=m1,m1<=12) # y=17,m1=4
# 平成17年4月
print(充足リスト(保険料納付猶予_若年1,50))
# [1757, 1758, 1759, 1760, 1761, 1762, 1763, 1764, 1765, 1766, 1767, 1768]
# 平成17年4月〜平成18年3月
