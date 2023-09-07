#Решение через костыль, но работает и с единицей
def guess(root):
    for number in range(1, 1000000):
        if root / number == number:
            print(root / number)
            break
        else:
            print(f'{number} НЕ ПОДОШЛО')

guess(1)