# setainushi_v5.py
# 世帯主の年金原簿　第九十条，九十条の二で参照
# f5の検証v5において，honnin_v5,haiguusha_v5と共に使用
from essentials import *

前年の所得が政令第六条の七で定める額以下=(lambda m: m==8)
前年の所得が政令第六条の八で定める額以下=(lambda m: Or(m==7,m==8))
前年の所得が政令第六条の九で定める額以下=(lambda m: False)
生活保護以外の厚生労働省令で定める援助を受給=(lambda m: False)
障害者であり前年の所得が政令で定める額以下=(lambda m: False)
寡婦であり前年の所得が政令で定める額以下=(lambda m:False)
天災など省令により保険料納付が著しく困難=(lambda m:False)
