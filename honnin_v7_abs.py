# honnin_v7_abs.py
# 第七条被保険者の検証で使用
from essentials import *

二十歳以上六十歳未満=(lambda d:True)
日本国内に住所を有する=(lambda d:between(D1,D2)(d))
厚生年金保険法老齢等受給可能=(lambda d:False)
厚生年金保険の被保険者=(lambda d:between(D3,D4)(d))
第二号被保険者の配偶者=(lambda d:between(D5,D6)(d))
主に第二号被保険者の収入により生計維持=(lambda d:between(D5,D6)(d))
