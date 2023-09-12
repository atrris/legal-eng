#####################
# honnin_v18_abs.py #
#####################

# 第十八条の検証で使用

from essentials import *

支給事由発生=(lambda d:d==D1)
受給権利消滅=(lambda d:d==D4)
停止事由発生=(lambda d:d==D2)
停止事由消滅=(lambda d:d==D3)
