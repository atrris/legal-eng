# v5.py
# 小型の年金原簿honnin_v5,haiguusha_v5,setainushi_v5のもとでの第五条の検証

import dummy
dummy.honnin='honnin_v5'
dummy.haiguusha='haiguusha_v5'
dummy.setainushi='setainushi_v5'
dummy.definitions='definitions_simple'

from f5 import *
import time
start=time.time()
m=20
L=充足リスト(保険料納付済期間,m)
print('保険料納付済期間',L)
L=充足リスト(保険料免除期間,m)
print('保険料免除期間',L)
L=充足リスト(保険料全額免除期間,m)
print('保険料全額免除期間',L)
L=充足リスト(保険料四分の三免除期間,m)
print('保険料四分の三免除期間',L)
L=充足リスト(保険料半額免除期間,m)
print('保険料半額免除期間',L)
L=充足リスト(保険料四分の一免除期間,m)
print('保険料四分の一免除期間',L)
print(time.time()-start, 'sec')

# 保険料納付済期間 [6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19]
# 保険料免除期間 [7, 8, 18]
# 保険料全額免除期間 [18]
# 保険料四分の三免除期間 []
# 保険料半額免除期間 [7, 8]
# 保険料四分の一免除期間 []
# 1.6096739768981934 sec
