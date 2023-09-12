# f18_specific.py　第十八条　年金の支給期間及び支払期月，個別版
# k:給付型パラメータ
from essentials import *
from specialization_a18 import * # 通則個別述語対応規則_第十八条

受給権月=(lambda k:期間(支給事由発生(k),受給権利消滅(k)))
支給=(lambda k:(lambda m:And(受給権月(k)(m),Not(停止(k)(m)))))
停止=(lambda k:期間(停止事由発生(k),停止事由消滅(k)))
年金支払額=(lambda k:(lambda m:
           If(偶数月(m),年金支給額(k)(m-2)+年金支給額(k)(m-1),0)))
年金支給額=(lambda k:(lambda m:If(支給(k)(m),年金額(k)(m),0)))
