# specialization_a18_AB
# 第十八条用通則個別述語結合規則 for 年金A,B
from honnin_AB import * #年金原簿_年金A,B
年金AB,(年金A,年金B)=EnumSort('AB',('A','B'))
# 以下，k:年金AB, d:日

支給事由発生=(lambda k:(lambda d:
            If(k==年金A,A年金受給権利発生(d),B年金受給権利発生(d))))
受給権利消滅=(lambda k:(lambda d:
            If(k==年金A,A年金受給権利消滅(d),B年金受給権利消滅(d))))
停止事由発生=(lambda k:(lambda d:
            If(k==年金A,B年金受給権利発生(d),A年金受給権利発生(d))))
停止事由消滅=(lambda k:(lambda d:
            If(k==年金A,Or(A年金停止解除申請(d),停止解除みなし申請(年金A)(d)),
                        Or(B年金停止解除申請(d),停止解除みなし申請(年金B)(d)))))
停止解除みなし申請=(lambda k:(lambda d:
            And(k==年金A,支給事由発生(年金B)(d)))) #補題AB
