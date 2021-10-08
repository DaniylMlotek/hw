str = int(input('enter how many stars:'))
print('*'*str)

for i in range(str - 1):
    print('*','' *(str - 2),'*')
    print('*'*str)