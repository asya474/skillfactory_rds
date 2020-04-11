import numpy as np
predict = np.random.randint(1,101)
i=0
left = 1
right = 100
while True:
    i+=1
    current = (left+right)//2
    if current == predict:
        print('Вы угадали с {} попытки!'.format(i))
        break
    elif current < predict:left = current + 1
    else:right = current - 1