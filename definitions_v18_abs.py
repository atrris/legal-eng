# definitions_v18_abs.py
from essentials import *

Day,(D1,D2,D3,D4)=EnumSort('Day',('D1','D2','D3','D4'))
p=Function('p',Day,Day,BoolSort())
x,y,z=Consts('x y z',Day)
orderDay=And(
        ForAll(x,p(x,x)),
        ForAll([x,y,z],Implies(And(p(x,y),p(y,z)),p(x,z))),
        ForAll([x,y],Implies(And(p(x,y),p(y,x)),x==y)),
        ForAll([x,y],Or(p(x,y),p(y,x))))
seqDay=And(p(D1,D2),p(D2,D3),p(D3,D4))

Month,(M1,M2,M3,M4,M11,M22,M33,M112,M223,M334,MM)= \
        EnumSort('Month',('M1','M2','M3','M4','M11','M22','M33', \
                          'M112','M223','M334','MM'))
q=Function('q',Month,Month,BoolSort())
u,v,w=Consts('u v w',Month)
orderMonth=And(
        ForAll(u,q(u,u)),
        ForAll([u,v,w],Implies(And(q(u,v),q(v,w)),q(u,w))),
        ForAll([u,v],Implies(And(q(u,v),q(v,u)),u==v)),
        ForAll([u,v],Or(q(u,v),q(v,u))))
seqMonth=And(q(M1,M11),q(M11,M112),q(M112,M2),q(M2,M22),q(M22,M223),
             q(M223,M3),q(M3,M33),q(M33,M334),q(M334,M4))

属月=(lambda d:If(d==D1,M1,If(d==D2,M2,If(d==D3,M3,If(d==D4,M4,MM)))))
次月=(lambda m:If(m==M1,M11,If(m==M2,M22,If(m==M3,M33,MM))))
期間=(lambda f,g:(lambda m:
        Exists(x,
            And(f(x),q(次月(属月(x)),m),
                ForAll(y,
                    Implies(And(g(y),p(x,y)),
                            q(m,属月(y))))))))
