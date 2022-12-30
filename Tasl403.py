# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

list_input=[3,5,8,4,6,9,5,4,8,1,7,4,8,0,8,6,11]
list_rezult=[]
print('original')

print(list_input)

unic_num_list=set(list_input)
for list_input  in  unic_num_list :

    list_rezult.append(list_input)
print('a sequence of non-repeating numbers')

print(list_rezult)


