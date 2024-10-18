input_data = open('input.txt', 'r')
output = open('output.txt', 'w')
data = input_data.read()
data = data.split()
a = int(data[0]) 
for i in range(2, 25_001): # Задаем i из списка 
    if a%i == 0 and i != a: # делаем условия для выполнения операции(проверка на проостоео число)
        output.write(str('N')) # выводим N
        break # завершаем цикл если условие выполнилось 
    elif i == a: # делаем условие, что i равно нашему числу 
        output.write(str('Y'))
if a == 1: # добавляем последнее условие если а равнор единице 
    output.write(str('N'))      
input_data.close()
output.close()