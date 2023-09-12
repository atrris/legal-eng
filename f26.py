# f26.py　第二十六条　支給要件

from essentials import *
from f5 import 保険料納付済期間,保険料免除期間
m=Int('m')
d1=Int('d1')

老齢基礎年金の支給要件成立=lambda d:\
            And(Exists(m,And(Or(保険料納付済期間(m),保険料免除期間(m)),
                             Not(保険料免除_学生(m)))),
                月数(保険料納付済期間)+月数(保険料免除期間)>=120,
                d==年齢到達日(65,誕生日))
