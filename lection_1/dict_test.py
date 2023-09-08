alphabet = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'X',
    10: 'Y',
    'Z': 10,
    True: 'sdasd',
    False: 123123,
    None: 'dasdasd',
}

O_letter = alphabet.get('Z', None)
if not bool(O_letter):
    print('NO O')

for key, value in alphabet.items(): # .keys() .values()
        print(f'Ключ: {key} Значение: {value}')