# v5_ladyA_date.py
# A女史の年金原簿honnin,haiguusha,setainusi_A_dateのもとでのf5のテスト

import time
import dummy
dummy.honnin='honnin_ladyA_date'
dummy.haiguusha='haiguusha_ladyA_date'
dummy.setainushi='setainushi_ladyA_date'
dummy.definitions='definitions_date_3'

from essentials import *
from f5 import *
start=time.time()
L=充足リスト(保険料納付済期間,500)
print('保険料納付済期間',list(map(mjm2ym,L)))
print(len(L),'\n')
#432

L=充足リスト(保険料免除期間,500)
print('保険料免除期間',list(map(mjm2ym,L)))
print(len(L),'\n')

L=充足リスト(保険料全額免除期間,500)
print('保険料全額免除期間',list(map(mjm2ym,L)))
print(len(L),'\n')

L=充足リスト(保険料四分の三免除期間,500)
print('保険料四分の三免除期間',list(map(mjm2ym,L)))
print(len(L),'\n')

L=充足リスト(保険料半額免除期間,500)
print('保険料半額免除期間',list(map(mjm2ym,L)))
print(len(L),'\n')

L=充足リスト(保険料四分の一免除期間,500)
print('保険料四分の一免除期間',list(map(mjm2ym,L)))
print(len(L),'\n')

print(time.time()-start,'sec')
