# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math 

d_num=input('Enter limit digital  number PI(example 0.01)=')
if 0.1>= float(d_num)>= 0.0000000001:
    print('PI='+str(math.pi))
    dig_num=len(str(d_num).split('.')[1])
    rezult_pi=round(math.pi,dig_num)
    print('With the number of decimal places '+ str(dig_num)+' signs,\nPI is equal to-> '+ str(rezult_pi))
else:
    print('Error,incorrect number entry')
    print('the number must be in the range -> $10^{-1} ≤ d ≤10^{-10}$')
