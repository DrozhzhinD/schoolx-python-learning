def outer():
    print (f' y in outer before assig: {"y" in locals()}')
    y=12
    print (f' y in outer after assig: {"y" in locals()}')
    def answer(x):
        return x
    return answer('')

if __name__ == '__main__':
    x = 42
    print(
        f' y in mail in exists: {"y" in locals()}'
    )
