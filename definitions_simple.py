#########################
# definitions_simple.py #
#########################

# 論理式記述を行うために必要となる補助的な関数や述語の定義集
# 日付に関しては，1月30日，1年12月と簡略化して計算を高速化
# 一般的なカレンダーに関するものは，definitions_dateに与えられている．

from essentials import *
d,d1,d2,d3=Ints('d d1 d2 d3')

# 老齢基礎年金改定率,平成30年
改定率=0.998

#### 論理演算子の述語演算子化 ####
# And,Or,NotなどのBool上の論理演算子を，通日に関する関数AND,OR,NOTとしたもの．
# 日付パラメータを使わずに，条文の言語表現に近い論理式化が可能となる．
# 内容的には，述語p,q,..,r:Int=>Boolに対して，
#   AND(p,q,..,r)==lambda d: And(p(d),q(d),..,r(d))
#   OR(p,q,..,r)==lambda d: Or(p(d),q(d),..,r(d))
#   NOT(p)==lambda d: Not(p(d))
#   IF(p,q,r)==lambda d: If(p(d),q,r)
# d:Intは，通日を表す変数

from functools import reduce
OR=(lambda *args:(lambda d:
      reduce(Or,[x(d) for x in args],False)))
AND=(lambda *args:(lambda d:
      reduce(And,[x(d) for x in args],True)))
NOT=lambda f:(lambda d:Not(f(d)))
IF=lambda p,q,r:lambda d:If(p(d),q,r)
FALSE=lambda d:False
TRUE=lambda d:True

### 日付けのための述語，関数 ###
# 西暦1年1月1日を起点とした日数，月数で日，月を表現
# 日付けに関しては，1年12月，1月30日　と簡単化

属月=lambda d:d/30 # 通日dの属する月
偶数月=lambda m:m%2==0

### 充足リスト ###
# f(i)を満たす最大m個のiからなるリスト

def 充足リスト(f,m):
    v=[]
    i,i0=Ints('i i0')
    s=Solver()
    p=f(i)
    s.add(p)
    for n in range(0,m):
        if s.check()==sat:
            i0=s.model()[i]
            v=v+[i0.as_long()]
            s.add(i!=i0)
        else:
            break
    return sorted(v)

# #### 月数　####
# 条件f(i)を満たすiを最大600個までカウント (年金額を計算するf27で使用．)
# 被保険者の資格に必要な480月（40年間）をカバー
# iごとにf(i)の成立を判定
# 月数(f)は 一階論理式ではなく，Pythonプログラムにより計算される数値であり，
# したがって，例えば，月数(f)==10　になるようにfに含まれるパラメータを
# ソルバに自動で解かせることは出来ない．

def 月数(f):
    m=600
    v=0
    i,i0=Ints('i i0')
    p=f(i)
    s=Solver()
    s.add(p)
    for n in range(0,m):
        if s.check()==sat:
            i0=s.model()[i]
            v=v+1
            s.add(i!=i0)
        else:
            break
    return v

####　期間　####
# 以下の３つの「期間」マクロ（期間，期間２，期間３）と「月内で最後に成立」では，
# （１）一階論理式によるものと，（２）内部でソルバーを呼び出すPython形式のものを
# 与えている．一階論理による定義は，実用的なサイズの問題には時間が掛かりすぎるが，
# 記号的検証が可能である．
#
# 一方，python形式のものは，大きなサイズの問題でも動作するが，
# 内部でソルバーを呼び出して充足リストの計算をしているので，f,gに含まれる
# パラメータの調整をソルバーに行わせるなどの柔軟な処理は出来ない．
# 以下で，f,g,h:日->{True,False}

## 期間
# 条件fを最初に満たす日d1の翌月から，条件gを最初に満たす日d2の属月まで月mの集合．
# （このようなmに対してTrueとなる述語）
# このようなf,gの対が複数ある場合は，それらの期間を合算したもの.
# ...f.....g....f.....g...
#    -     -    =     =

# 一階論理式版
# 期間=(lambda f,g:(lambda m:
#     Exists(d1,
#        And(f(d1),属月(d1)+1<=m,
#            ForAll(d2,
#               Implies(And(g(d2),d1<=d2),
#                       m<=属月(d2)))))))

# Python版
# f成立=>g成立時点を取り出し，その間の区間をOrで合算して期間を構成している．
# kは区間の最大数である．

def 期間(f,g):
    def term(m):
        k=100
        p=False
        Lf=充足リスト(f,k)
        Lg=充足リスト(g,k)
        while Lf!=[]:
            m1=属月(Lf[0])
            m2=属月(Lg[0])
            p=Or(p,If(m1==m2,m==m1,And(m1<m,m<=m2)))
            Lf=Lf[1:]
            Lg=Lg[1:]
        return p
    return term

##　期間2
# fが成立に至った日の属月から、gが成立に至った日の前月までの月からなる期間
# ただし，fの成立した後で同じ月にgが成立したときには，その月は含める．
# このようなペアが複数ある場合はそれらの期間の集合

# logic 版
#
# 期間2=(lambda f,g:(lambda m:
#     Exists(d1,
#        And(f(d1),属月(d1)<=m,
#            Or(ForAll(d2,
#                 Implies(And(g(d2),d1<=d2),
#                         m<=属月(d2)-1)),
#               And(属月(d1)==m,
#                   Exists(d2,And(g(d2),属月(d2)==m))))))))

# Python版

def 期間2(f,g):
    def term2(m):
        k=100
        p=False
        Lf=充足リスト(f,k)
        Lg=充足リスト(g,k)
        while Lf!=[]:
            m1=属月(Lf[0])
            m2=属月(Lg[0])
            p=Or(p,If(m1==m2,m==m1,And(m1<=m,m<m2)))
            Lf=Lf[1:]
            Lg=Lg[1:]
        return p
    return term2

##　期間3
# fが成立する日の前月から、fが成立しなくなる日の月までの月の集合

# logic 版
# 期間3=(lambda f:(lambda m:
#     Exists(d1,
#        And(f(d1),属月(d1)-1<=m,
#            ForAll(d2,
#               Implies(And(Not(f(d2)),d1<=d2),
#                       m<=属月(d2)))))))

# Python版

def 期間3(f):
    h1=成立に至る(f)
    h2=成立に至る(NOT(f))
    def term3(m):
        k=100
        p=False
        Lh1=充足リスト(h1,k)
        Lh2=充足リスト(h2,k)
        while Lh1!=[]:
            m1=属月(Lh1[0])
            m2=属月(Lh2[0])
            p=Or(p,And(m1-1<=m,m<=m2))
            Lh1=Lh1[1:]
            Lh2=Lh2[1:]
        return p
    return term3

###　事由の成立関係　###
# 月mのうちで，条件fが成立する日dがあり，その後g,hが成立する日はない．

# logic版
# 月内で最後に成立=(lambda f,g,h:(lambda m:
#     Exists(d,
#         And(m==属月(d),
#             f(d),
#             ForAll(d1,
#                 Implies(And(d<=d1,m==属月(d1)),
#                         Not(Or(g(d1),h(d1)))))))))

# Python版
def 月内で最後に成立(f,g,h):
    f1=lambda d:And(Not(f(d-1)),f(d))
    f2=lambda d:And(f(d),Not(f(d+1)))
    g1=lambda d:And(Not(g(d-1)),g(d))
    h1=lambda d:And(Not(h(d-1)),h(d))
    def term4(m):
        k=100
        p=False
        Lf1=充足リスト(f1,k)
        Lf2=充足リスト(f2,k)
        Lg1=充足リスト(g1,k)
        Lh1=充足リスト(h1,k)
        while Lf1!=[]:
            m1=属月(Lf1[0])
            m2=属月(Lf2[0])
            for d in Lg1+Lh1:
                if Lf2[0]<d and m2==属月(d):
                    m2=m2-1
                    break
            p=Or(p,And(m1<=m,m<=m2))
            Lf1=Lf1[1:]
            Lf2=Lf2[1:]
        return p
    return term4

#　事由の成立
成立に至る=lambda f:lambda d: And(Not(f(d-1)),f(d))
過去に成立 = lambda f: lambda d:Exists(d1,And(d1<=d,f(d1)))
初めて成立 = lambda f: lambda d:And(f(d),
                                  ForAll(d1,Implies(f(d1),d<=d1)))

#　事由成立の前後関係
before=lambda d:lambda g:Exists(d2,And(g(d2),d2<d))
after=lambda d:lambda g:Exists(d2,And(g(d2),d<d2))
between=(lambda d1,d3:lambda g:
        Exists(d2,And(g(d2),d1<=d2,d2<=d3)))
