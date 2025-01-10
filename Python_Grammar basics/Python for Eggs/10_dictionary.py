'''
dic = {}
dic['dictionary'] = '1. A reference book containing an ...'
dic['python'] = 'A snake of Plato'

del dic['python'] #딕셔너리 삭제

print(dic)

'''

family = {'mom': 'Park', 'dad': 'Choi', 'daughter': 'Conzato'}
family['dad'] = 'Yoon'
print(family)


#연습 문제 1

def korean_number(x):
    korean = {1: '일', 2: '이', 3: '삼', 4: '사', 5: '오',
              6: '육', 7:' 칠', 8: '팔', 9: '구'}
    
    return korean[x]

print(korean_number(3))


#연습 문제 2
four_maxims = {'江湖之樂(강호지락)': '자연을 벗 삼아 누리는 즐거움',
'欲速不達(욕속부달)': '빨리 하고자 하면 이루지 못함',
'積小成大(적소성대)': '작은 것을 쌓아 큰 것을 이룸',
'勤儉節約(근검절약)': '부지런하고 알뜰하게 재물을 아낌',
'經世濟民(경세제민)': '세상을 다스리고 백성을 구제함',
'塞翁之馬(새옹지마)': '인생의 길흉화복은 변화가 많아서 예측하기가 어려움',
'好事多魔(호사다마)': '좋은 일에는 흔히 방해되는 일이 많음',
'桑田碧海(상전벽해)': '세상일의 변천이 심함',
'自業自得(자업자득)': '자기가 저지른 일의 결과를 자기가 받음',
'因果應報(인과응보)': '원인과 결과가 상응하여 보답한다',
'愚公移山(우공이산)': '어떤 일이든 끊임없이 노력하면 반드시 이루어짐}'}


for lines in four_maxims:
    press_enter = input('Enter를 누르세요...: ')
    print(lines)