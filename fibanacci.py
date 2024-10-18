input_data = open('input.txt', 'r')
output_data = open('output.txt', 'w')
n = input_data.readline()
# Вводим значения (2) первых членов последовательности
a = 0
b = 1
# Выводим значения двух первых членов последовательности через запятую
output_data.write(str(a))
output_data.write(", ")
output_data.write(str(b))
output_data.write(", ")
for i in range(2, int(n) + 1): # Переприсваеваем n-ому и n+1-ому члену значения n+1-ого и n+2-ого
    a, b = b, a + b # Выводим в файл новое значение переменной b (она сейчас равна n+2-ому члену)
    output_data.write(str(b))
    # Расставляем запятые
    if i != (int(n)):
        output_data.write(", ")
input_data.close()
output_data.close()