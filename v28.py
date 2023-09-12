# v28.py
# honnin_v28, definitons_v28のもとでの支給の繰下の検証

import dummy
dummy.honnin='honnin_v28'
dummy.definitions='definitions_v28'

from essentials import *
from f28 import * #第二十八条 支給の繰下げ
dd=Int('dd')
s=Solver()
s.add(支給繰下げ申請みなし日(dd))
print(s.check()) # sat
print(s.model())
# [dd = 6]
