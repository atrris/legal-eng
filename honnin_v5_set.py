# honnin_v5_set.py　第五条の検証で使用
# 述語をそれが成立する日や月のpython setとして表現した。残念ながら、
# 検証の過程で unhashable dateとして失敗する。

from essentials import *

between=lambda m,n: {d for d in range(m,n+1)}

# 第七条関連
年齢=(lambda d:26+d/360)
二十歳以上六十歳未満=lambda d: And(20<=年齢(d),年齢(d)<60)
日本国内に住所を有する=lambda d: d in between(200,600)
厚生年金保険法老齢等受給可能=lambda d: False
厚生年金保険の被保険者=lambda d: d in between(300,500)
第二号被保険者の配偶者=lambda d: d in between(400,550)
主に第二号被保険者の収入により生計維持=lambda d:d in between(400,550)

# 保険料納付状況
保険料納付済=lambda m: m in {6,9,19}
残りの四分の一納付済=lambda m:False
残りの半額納付済=lambda m:m in {7,8}
残りの四分の三納付済=lambda m:False
追納により納付とみなされる期間=lambda m:False

# 保険料免除関係

# 家族関係
世帯主が本人以外=(lambda m:False)
配偶者がいる=(lambda m:False)
#第八十九条関係
障害基礎年金の受給権者=(lambda d:False)
厚生年金保険法に基づく障害を支給事由とする年金給付の受給者=(lambda d:False)
障害を支給事由とする政令で定める給付の受給権者=(lambda d:False)
最後に障害状態に該当しなくなつた日から三年を経過=(lambda d: False)
障害状態にない=(lambda d:False)
政令で定める者=(lambda d:False) # 国民年金法施行令第六条の五第二項
生活保護法の生活扶助を受けている者=(lambda d:False)
厚生労働省令施設の入所者=(lambda d:False)
納付不要保険料納付申出=(lambda m:False)

#第九十条，九十条の二，九十条の三関係
前年の所得が政令_施行令第六条の七で定める額以下=(lambda m:False)
前年の所得が政令_施行令第六条の八で定める額以下=(lambda m: m in {7,8})
前年の所得が政令_施行令第六条の九で定める額以下=(lambda m:False)
生活保護以外の厚生労働省令で定める援助を受給=(lambda m:False)
障害者であり前年の所得が政令で定める額以下=(lambda m:False)
寡婦であり前年の所得が政令で定める額以下=(lambda m:False)
天災などにより保険料納付が著しく困難=(lambda m: m in {18})

#保険料法定免除期間=(lambda m: False)
保険料全額申請免除期間=(lambda m: False)
保険料四分の三免除期間=(lambda m: False)
保険料半額免除期間=(lambda m: m in {7,8})
保険料四分の一免除期間=(lambda m: False)
#保険料免除_学生期間=(lambda m:m==18)
学生等=(lambda m: m in {18})
