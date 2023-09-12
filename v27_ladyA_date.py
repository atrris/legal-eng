# v27_date
# 年金原簿honnin_A_dateのもとでの年金額の計算
import dummy
dummy.honnin='honnin_ladyA_date'
dummy.haiguusha='haiguusha_ladyA_date'
dummy.setainushi='setainushi_ladyA_date'
dummy.definitions='definitions_date_3'

import time
start=time.time()
from essentials import *
from f27 import *

print("保険料納付済月数",保険料納付済月数)
print("保険料四分の一免除月数",保険料四分の一免除月数)
print("保険料半額免除月数",保険料半額免除月数)
print("保険料四分の三免除月数",保険料四分の三免除月数)
print("保険料全額免除_学生を除く月数",保険料全額免除_学生を除く月数)
print("合算月数",合算月数)
print("減額係数",減額係数)
print("老齢基礎年金額", 老齢基礎年金額)
print(time.time()-start,"sec")

# 保険料納付済月数 432
# 保険料四分の一免除月数 0
# 保険料半額免除月数 12
# 保険料四分の三免除月数 0
# 保険料全額免除月数_学生を除く 0
# 合算月数 441.0
# 減額係数 0.91875
# 老齢基礎年金額 716000
# 3.9343130588531494 sec
