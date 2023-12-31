# f90.py　第九十条 保険料免除(全額,申請免除)
from essentials import *

保険料全額免除要件=(lambda m:
           And(Not(Or(保険料四分の三免除(m),
                      保険料半額免除(m),
                      保険料四分の一免除(m),
                      保険料納付済(m),
                      学生等(m))),
               本人世帯主配偶者が経済的困窮(m)))

経済的困窮=(lambda p:lambda m:
           Or(p.前年の所得が政令第六条の七で定める額以下(m),
              p.生活保護以外の厚生労働省令で定める援助を受給(m),
              p.障害者であり前年の所得が政令で定める額以下(m),
              p.寡婦であり前年の所得が政令で定める額以下(m),
              p.天災など省令により保険料納付が著しく困難(m)))

# 以下に於いて，本人，世帯主，配偶者は，それぞれの年金原簿を表し，essentialsにおいて
# import される．

本人世帯主配偶者が経済的困窮=(lambda m:
           And(経済的困窮(本人)(m),
               Implies(世帯主が本人以外(m),経済的困窮(世帯主)(m)),
               Implies(配偶者がいる(m),経済的困窮(配偶者)(m))))

########
# 以下をf90に加えることも可能である．しかし，内容が細部に亘るので，事前にその評価を行い，
# その結果によってhonninを変更してからf90に入る方が良いと思われる．

# import seirei6_7 as 政令第六条の七
#
# 前年の所得が政令第六条の七で定める額以下=lambda m:\
#            前年度の所得(m) <= 政令第六条の七.定める額
# 前年度の所得=lambda m: If(And(1<=m,m<=省令で定める月),
#                         所得(属年(m)-2),所得(属年(n)-1))

######
# seirei6_7.py
# 定める額=35*(本人.扶養親族の数+1)+22
