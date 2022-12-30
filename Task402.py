# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

natur_num=int(input('Enter nanural number N= '))
list_nnum=[]
nums=natur_num

for i in range(2,int(natur_num)):
    if nums%i==0 and nums!=i:
        list_nnum.append(i)
        nums=nums/i

if natur_num>2 :
    list_nnum.append(int(nums))
if list_nnum[0]==int(natur_num):
    print('Number is natural= '+str(list_nnum[0]))
    
if len(list_nnum)>1:
    print(list_nnum)