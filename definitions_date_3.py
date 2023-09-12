#########################
# definitions_date_3.py #
#########################

# 論理式記述を行うために必要となる補助的な関数や述語の定義集
# 西暦による日付表記に対応

from essentials import *
d,d1,d2,d3=Ints('d d1 d2 d3')
y,m,m1,m2,mjd=Ints('y m m1 m2 mjd')

#### 老齢基礎年金改定率,平成30年 ####
改定率=0.998

#### 論理式記述に表れる日付，日付表示 ####
# 日付：ある起点からの日数，月数，年数を用いて表す．
# これらを，通日，通月，通年と呼ぶ．
# 起点となる日は基本的には任意であるが，修正ユリウス通日では1858年11月17日を用いている．
# 本書でもこれを用いる．
# 日付表記：西暦による．和暦に関しては，年号のみを扱う関数を用いる．

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

OR=(lambda *args:lambda d:
      reduce(Or,[x(d) for x in args],False))
AND=(lambda *args:lambda d:
      reduce(And,[x(d) for x in args],True))
NOT=lambda f:lambda d:Not(f(d))
IF=lambda p,q,r:lambda d:If(p(d),q,r)
FALSE=lambda d:False
TRUE=lambda d:True

#### 日付けに関する述語，関数 ####
# 以下，「通日」，「通月」は，関数名とデータ集合名に同じ名前を使っている．
# 年，月，日，通日，通月，誕生日，年齢：Int
# 通日：年x月x日 => 通日
# 通月：年x月　=> 通月
# Year：通日 => 年
# Month：通日 => 月
# Day：通日 => 日
# YMD：通日　=>　年x月x日
# 属月：通日 => 通月
# 属年：属月 => 通年
# 年齢：誕生日 => 通日 => 年齢
# 年齢到達日：年齢ｘ誕生日 => 通日
# 年齢到達：(年齢ｘ誕生日)x通日 => Bool
# 昭和，平成，令和：和暦年 => 西暦年

quot=lambda a,b:(a-a%b)/b
# z3では，Int a,bのとき整数除算, Python中の実行では実数除算に注意

# 以下，通日，Year, Month, Dayの定義は，Wikipediaによる．

def 通日(y,m,d):
        y1=If(m<=2,y-1,y)
        m1=If(m<=2,m+12,m)
        d1=quot(36525*y1,100)
        d2=quot(y1,400)
        d3=quot(y1,100)
        m2=quot(3059*(m1-2),100)
        mjd=d1+d2-d3+m2+d-678912
        return mjd

def Year(mjd):
        n=mjd+678881
        a2=quot(4*(n+1),146097)+1
        a1=quot(3*a2,4)
        a=4*n+3+4*a1
        b1=quot((a%1461),4)
        b=5*b1+2
        y1=quot(a,1461)
        m1=quot(b,153)+3
        y=If(m1>=13,y1+1,y1)
        return y

def Month(mjd):
        n=mjd+678881
        a2=quot(4*(n+1),146097)+1
        a1=quot(3*a2,4)
        a=4*n+3+4*a1
        b1=quot((a%1461),4)
        b=5*b1+2
        m1=quot(b,153)+3
        m=If(m1>=13,m1-12,m1)
        return m

def Day(mjd):
        n=mjd+678881
        a2=quot(4*(n+1),146097)+1
        a1=quot(3*a2,4)
        a=4*n+3+4*a1
        b1=quot(a%1461,4)
        b=5*b1+2
        d=quot(b%153,5)+1
        return d

def YMD(mjd):
        s=Solver()
        s.add(Year(mjd)==y,Month(mjd)==m,Day(mjd)==d)
        s.check()
        y1=s.model()[y]
        m1=s.model()[m]
        d1=s.model()[d]
        return (y1,m1,d1)

mjd2ymd=YMD

通月=lambda y,m:(y-1858)*12+m-11

# Pythonの中でのみ有効
def mjm2ym(mjm): # 通月=>年ｘ月
    m=(mjm+10)%12+1
    y=(mjm-m+11)//12+1858
    return (y,m)

# Z3版，Pythonで使うとy:realとして出力
def YM(mjm): # 通月=>年ｘ月
    m=(mjm+10)%12+1
    y=quot(mjm-m+11,12)+1858
    return (y,m)

# 通日dの属する通月
属月=lambda d:(Year(d)-1858)*12+Month(d)-11
# 通月mの属する通年
属年=lambda m:quot((m+10),12)+1858

偶数月=lambda m:m%2==1  # m:通月，通月は1858年11月が起点
前月=lambda f:lambda m:Exists(d,And(f(d),属月(d)==m+1))
# fの成立する日の属する月の前月

# 和暦年 => 西暦年
昭和=lambda y:y+1925
平成=lambda y:y+1988
令和=lambda y:y+2018

#### 日の区間，月の区間，当日，当月####
# 以下，x,x1,x2: (年,月,日) or (年，月)，d:日，m:月

区間=lambda u,v:lambda w:And(u<=w,w<=v)

DD=lambda x1,x2:区間(通日(x1[0],x1[1],x1[2]),通日(x2[0],x2[1],x2[2]))
# DD((1977,4,1),(1998,9,30))
#           ==lambda d:And(通日(1977,4,1)<=d,d<=通日(1996,9,30))

MM=lambda x1,x2:区間(通月(x1[0],x1[1]),通月(x2[0],x2[1]))
# MM((1955,5),(1977,3))==lambda m:And(通月(1955,5)=<m,m=<通月(1977,3))

D=lambda x:lambda d:d==通日(x[0],x[1],x[2])
M=lambda x:lambda m:m==通月(x[0],x[1])
# D((1977,4,1))==lambda d:d==通日(1977,4,1)
#      通日(1977,4.1)にのみTrueになる述語

#### 年齢関連 ####
# 年齢：誕生日がbirthdayである人の通日dにおける年齢age
# Int => Int => Int

def 年齢(birthday): # birthday:通日
    def 年齢1(d):
        y=Year(d)
        a=y-Year(birthday)
        mjd=通日(y,Month(birthday),Day(birthday))
        age=a-If(d<mjd-1,1,0)
        return age
    return 年齢1

# 年齢到達: 誕生日がbirthdayの人がage歳になる日dにのみTrueになる述語
# 年齢到達日: その日を与える関数
# 民法の年齢に関する規定で，誕生日の前日に年齢が加算される．

年齢到達=(lambda age,birthday:lambda d:
        d==通日(Year(birthday)+age,Month(birthday),Day(birthday)-1))
年齢到達日=(lambda age,birthday:
        通日(Year(birthday)+age,Month(birthday),Day(birthday)-1))
年齢到達月=lambda age,birthday:属月(年齢到達日(age,birthday))

#### 充足リスト ####
# f(i)を満たす相異なる最大m個のソートされたiからなるリスト

def 充足リスト(f,m):
    v=[]
    i,i0=Ints('i i0')
    p=f(i)
    s=Solver()
    s.add(p)
    for n in range(0,m):
        if s.check()==sat:
            i0=s.model()[i]
            v=v+[i0.as_long()]
            s.add(i!=i0)
        else:
            break
    return sorted(v)

#### 月数　####
# 条件f(i)を満たすiを最大600個までカウント (年金額を計算するf27などで使用)
# 被保険者の資格に必要な480月（40年間）をカバー
# iごとにf(i)の成立を判定
# 月数(f)は 一階論理式ではなく，Pythonプログラムにより計算される数値であり，
# したがって，例えば，月数(f)==10　になるようにfに含まれるパラメータを
# ソルバーに自動で解かせることは出来ない．

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

# 一方，以下の「月数」は，600月分の式If(f(i),1,0)を+で結合したもの．
# 月数を得るには，最後に一気に充足性判定により数値を計算する．
# fが簡単なものでないとこの「If加算形式」のサイズが大きくなりすぎ，充足性判定に時間が掛かりすぎる．
# しかし，サイズMの小さい記号的検証では,fのパラメータの調整をこの方式により行うことが可能である．

# def 月数(f):
#     M=600
#     m=0
#     for n in range(0,M):
#         m=m+If(f(n),1,0)
#     return m
#
# 月数(f)=0+If(f(0),1,0)+If(f(1),1,0)+...+If(f(599),1,0)
# f=lambda d:d*d*d<1000
# v=Int('v')
# solve(月数(f)==v)
# v=10

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
# 条件fを最初に満たす日d1の翌月から，条件gを最初に満たす日d2の属月まで月mの集合
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
# f成立時点からg成立時点までを取り出し，その間の区間をOrで合算して期間を構成している．
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

# 一階論理式版
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

# 一階論理式版
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

####　事由の成立関係　####

## 月内で最後に成立
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
# 以下のものは，fがg,hと同時には成立しない,即ち,f(d)がg(d)やh(d)と共に成立する
# dが存在しない場合について，上記を最適化したPythonプログラムであり，月mの内で
# fが最後に成立するmを表す論理式を与える．

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

## 事由の成立

成立に至る=lambda f:lambda d: And(Not(f(d-1)),f(d))
過去に成立 = lambda f:lambda d:Exists(d1,And(d1<=d,f(d1)))
初めて成立 = lambda f:lambda d:And(f(d),
                                 ForAll(d1,Implies(f(d1),d<=d1)))

## 事由成立の前後関係
# before: 日dより前にgが成立する日がある．

before=lambda d:lambda g:Exists(d2,And(g(d2),d2<d))
after=lambda d:lambda g:Exists(d2,And(g(d2),d<d2))
between=(lambda d1,d3:lambda g:
        Exists(d2,And(g(d2),d1<=d2,d2<=d3)))
