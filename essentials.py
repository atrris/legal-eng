# essentials.py
# z3モジュール，年金銀簿モジュールおよびdefinitonsモジュールをimport

from z3 import *
from dummy import honnin,honnin_post,haiguusha,setainushi,definitions
exec('from '+definitions+' import *')
exec('import '+honnin+' as 本人')
exec('import '+honnin_post+' as 本人_post')
exec('import '+haiguusha+' as 配偶者')
exec('import '+setainushi+' as 世帯主')
exec('from '+honnin+' import *')
