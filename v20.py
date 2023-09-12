# v20.py
# 年金A,B（年金原簿honnin_AB）を対象とした第二十条「併給の調整」に関する検証
import dummy
dummy.definitions='definitions_simple'

from f18_specific import * #第十八条年金の支給期間，通則版
d,m=Ints('d m')

# 年金A,Bが同じ月mに支給されることがあることの検証
s=Solver()
s.add(And(支給(年金A)(m),支給(年金B)(m)),m==351)
print(s.check())  #sat
print(s.model())  #[m=351]
#print(充足リスト(AND(支給(年金A),支給(年金B)),100))
# 月351は年金A,Bともに支給される。

# 補題AB, 停止解除みなし申請の定義に必要(in specialization_a18_AB)
r=Solver()
for k in [年金A,年金B]:
   r.add(ForAll(d,
            Implies(And(k==年金A,支給事由発生(年金B)(d)),
                And(停止事由発生(k)(d),支給(k)(属月(d))))))
print(r.check())  # sat　補題ABは成立
