# v26_ladayA_date.py
# 第二十六条　支給要件
# honnin_ladyA_dateの支給要件の確認

import dummy
# 検証で使用する年金原簿モジュール，definitionsモジュールを設定
dummy.honnin='honnin_ladyA_date'
dummy.haiguusha='haiguusha_ladyA_date'
dummy.setainushi='setainushi_ladyA_date'
dummy.definitions='definitions_date_3'

import time
start=time.time()

from essentials import * # z3, 年金原簿，用語定義集をimport
from f26 import 老齢基礎年金の支給要件成立

start=time.time()
d,d1=Ints('d d1')
s=Solver()
s.add(老齢基礎年金の支給要件成立(d))
print(s.check())
x=s.model()[d].as_long()
print(YMD(x))
print(time.time()-start,"sec")
# sat
# (2020, 5, 9)
# 5.95085883140564 sec  definition_date_3の時
