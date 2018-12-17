alp = 'abcdefghijklmnopqrstuvwxyz'
input_string = input("Введите текст для зашифрования:")
input_step = int(input("Шаг:"))
result = ''
check = False


for letter_in_input_string in input_string:
    for letter_in_alp in alp:
        if letter_in_input_string == letter_in_alp:
            check = True

    if check == True:
        if alp.index(letter_in_input_string) + input_step < len(alp):
            result += alp[alp.index(letter_in_input_string) + input_step]
        else:
            result += alp[alp.index(letter_in_input_string) + input_step - len(alp)]
        check = False
    else:
        result += letter_in_input_string
print('Result:' + result)