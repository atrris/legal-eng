################
# honnin_v7.py #
################

# この年金原簿は，第七条，第八条，第九条，第十一条の検証で使用される．
# 日dは，26才の誕生日を起点とする通日で表現．1年360日，1月30日と簡単化
# なお，「年齢」の扱いに関しては，一般的なものがdefinition_date_3に与えられている．

from essentials import *

年齢=(lambda d:26+d/360)
二十歳以上六十歳未満=(lambda d:And(20<=年齢(d),年齢(d)<60))
日本国内に住所を有する=(lambda d:And(200<d,d<600))
厚生年金保険法老齢等受給可能=(lambda d:False)
厚生年金保険の被保険者=(lambda d:And(300<d,d<500))
第二号被保険者の配偶者=(lambda d:And(400<d,d<550))
主に第二号被保険者の収入により生計維持=(lambda d:And(500<=d,d<550))

#    *----日本在住---------------------------------------------------*
#    |                                                              |
#    |            *----企業に勤務---------------*                    |
#    |            |                            |                    |
#    |            |             *----結婚-----------------*         |
#    |            |             |              |          |         |
# ---*------------*-------------*--------------*----------*---------*------
# d=201          301           401            499        549       599
#    |            |                            |          |         |
#    *--第一号----**----------第二号-------------**-第三号---**-第一号--*
# m= 6           9 10                    15      16   17     18    19

# なお，以下はhonnin_v7を第十一条期間の検証で用いた場合の各被保険者期間を示す．

# 第一号被保険者期間 [6, 7, 8, 9, 18, 19]
# 第二号被保険者期間 [10, 11, 12, 13, 14, 15]
# 第三号被保険者期間 [16, 17]
