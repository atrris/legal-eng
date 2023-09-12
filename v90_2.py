# v90_2
# 異なる種別の免除期間が同じ月に関しては両立しないことを
# 年金原簿honnin_ladyA_dateについて確認したもの

import dummy
dummy.honnin='honnin_ladyA_date' # 本人
dummy.setainushi='setainushi_ladyA_date' # 世帯主
dummy.haiguusha='haiguusha_ladyA_date' # 配偶者
dummy.definitions='definitions_date_3'

from essentials import *
from f5 import *

m=Int('m')
s=Solver()
p=And(保険料四分の一免除期間(m),保険料半額免除期間(m))
s.add(p)
print(s.check())
# unsat
