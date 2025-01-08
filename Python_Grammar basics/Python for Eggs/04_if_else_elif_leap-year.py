year = int(input('연도를 입력하세요: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            result = '윤년'
        else:
            result = '평년'
    else:
        result = '윤년'
else:
    result = '평년'

print(result)