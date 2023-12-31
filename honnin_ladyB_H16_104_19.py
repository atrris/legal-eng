# honnin_ladyB_H104.py
# 附則H16_104テスト用


# B女史略歴
# 1975.5.10 誕生
# 1993.4.1-1997.3.31 大学生
# 1997.4.1-2003.9.30 会社勤務
# 2003.10.1-2008.1.31  自営業
# 2003.10-2008.1     保険料未納

from essentials import *

# 年齢関係
誕生日=通日(1975,5,10)

# 家族関係(月単位)
世帯主が本人以外=MM((1993,4),(1997,3))

配偶者がいる= FALSE

# 第七条被保険者の資格関係(日単位)
二十歳以上六十歳未満=DD((1995,5,9),(2035,5,8))
日本国内に住所を有する=DD((1975,5,10),(2008,1,20))
厚生年金保険法老齢等受給可能=FALSE
厚生年金保険の被保険者=DD((1997,4,1),(2003,9,30))
第二号被保険者の配偶者=FALSE
主に第二号被保険者の収入により生計維持=FALSE

#保険料納付関係
保険料納付済=FALSE
保険料前納=FALSE

## 保険料免除関係
保険料全額免除=FALSE
保険料半額免除=FALSE
学生等=MM((1993,4),(1997,3))

#第九十条，九十条の二，九十条の三関係
前年の所得が政令_施行令第六条の七で定める額以下=FALSE
生活保護以外の厚生労働省令で定める援助を受給=FALSE
障害者であり前年の所得が政令で定める額以下=FALSE
寡婦であり前年の所得が政令で定める額以下=FALSE
天災などにより保険料納付が著しく困難=MM((2005,4),(2006,3))
