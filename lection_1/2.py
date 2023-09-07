numbers: list = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
]

# for n in numbers:
#     if n % 3 == 0:
#         print(f'Число -{n} кратно 3')
#     if n % 3 != 0:
#         print(f'Число -{n} не кратно 3')

# for n in numbers:
#     if n % 2 ==0:
#         print(f'Число - {n} четное')
#     else:
#         print(f'Число - {n} нечетное')

# word: str = input('Введите слово: ')
# vowel: str = 'aeiou'

# vowel_count: int = 0
# for ch in word:
#     if ch in vowel:
#         vowel_count += 1

# print(vowel_count)

n: int = int(input('N: '))

for i in range(n+1):
    print(i)