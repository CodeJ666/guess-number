import random
count = 0 #猜的次數
r = random.randint(1, 100)
while True:
    count = count + 1
    num = input('請猜數字: ')
    num = int(num)
    if num == r:
        print('猜對了!')
        print('這是你猜的第', count, '次')
        break
    elif num > r:
        print('比答案大! 請繼續猜!')
    elif num < r:
        print('比答案小! 請繼續猜!')
    print('這是你猜的第', count, '次')