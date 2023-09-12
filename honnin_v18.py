# honnin_v18.py
# 第十八条の検証で使用

from essentials import *

支給事由発生=(lambda d:d==10000)
受給権利消滅=(lambda d:d==14000)
停止事由発生=(lambda d:Or(d==10500,d==12500))
停止事由消滅=(lambda d:Or(d==10520,d==13000))
年金額=(lambda m:70000)
