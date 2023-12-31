# f28.py　第二十八条 支給の繰下げ

# 各種年金に関する受給権が以下の述語として年金原簿honninに記録されていると仮定
# 　　老齢基礎年金の受給権者,障害基礎年金の受給権者,遺族基礎年金の受給権者
# 　　老齢を支給事由とするものを除く厚生年金の受給権者,付加年金の受給権者

from essentials import *

支給繰下げ申出可能=(lambda d:
      And(Not(老齢基礎年金請求日<六十六才に達した日),
          Not(他の年金給付の受給権者(六十五才に達した日)),
          Not(between(六十五才に達した日+1,六十六才に達した日)
                          (他の年金給付の受給権者となった)),
          老齢基礎年金の受給権者(d)))

支給繰下げ申請みなし日=(lambda d:
      Implies(And(支給繰下げ申出可能(支給繰下げ申出日),
                  六十六才に達した日<支給繰下げ申出日),
              If(before(七十才に達した日)(他の年金給付の受給権者となった),
                   他の年金給付の受給権者となった(d),
                   If(七十才に達した日<支給繰下げ申出日,
                      d==七十才に達した日,
                      d==支給繰下げ申出日))))

他の年金給付の受給権者=(lambda d:
       And(Or(障害基礎年金の受給権者(d),
              遺族基礎年金の受給権者(d),
              老齢を支給事由とするものを除く厚生年金受給権者(d)),
           Not(付加年金の受給権者(d))))

他の年金給付の受給権者となった=成立に至る(他の年金給付の受給権者)
