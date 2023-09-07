array = list(map(int, input('Введите массив чисел: ').split()))  
 
indexes = []  
for i in range(1, len(array)):  
    if array[i] - array[i-1] > 1:   
        indexes.append(i)  
 
if len(indexes) == 0:   
    print('Не найдено')   
else:   
    print(indexes)