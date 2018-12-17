alp = 'abcdefghijklmnopqrstuvwxyz'
input_string = input("Введите текст для зашифрования:")
input_step = int(input("Шаг:"))
result = ''

for c in input_string:
    if alp.index(c) + input_step < len(alp):
        result += alp[alp.index(c) + input_step]
    else:
        result += alp[alp.index(c) + input_step - len(alp)]

print('Result: ' + result)