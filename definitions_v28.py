# definitions_v28.py
# v28においてhonnin_v28とともにf28の検証で使われることを前提

from z3 import *
from essentials import *
d1,d2,d3=Ints('d1 d2 d3')
d=Int('d')

成立に至る=(lambda f:(lambda d: And(Not(f(d-1)),f(d))))
before=lambda d:lambda g:Exists(d1,And(g(d1),d1<d))
between=lambda d1,d2:lambda f:Exists(d,And(f(d),d1<=d,d<=d2))
年齢到達日=lambda age,birth:2*age-birth
