''' from tkinter import *

Widget = Label(None, text='I love Python')
Widget.pack()

from importlib import reload

'''

#연습 문제 1

'''
import calendar  ##문제 1
print(dir(calendar))

print([x for x in dir(calendar) if 'leap' in x])
## ['isleap', 'leapdays'] #문제 2

print(help(calendar.isleap))

'''

#연습 문제 2

'''
def hypotenuse(a, b):
    c2 = a ** 2 + b ** 2
    c = c2 ** (1/2)

    return print(c)

hypotenuse(3, 4)

'''

#연습 문제 3

##1
'''
import calendar
c = calendar.TextCalendar()
m = c.formatmonth(2021, 3)
print(m)

##2
import tkinter as tk

s = "Life is short\nUse Python"

root = tk.Tk()
t = tk.Text(root, height=7, width=20)
t.insert(tk.END, m)
t.pack()
tk.mainloop()

'''

#연습 문제 4
import sys

sys.path.append("../ch03")
import ridereader


rides = '''와일드 윙: 110cm 이상
드림보트: 120cm 이상
자이안트 루프: 120cm 이상
툼 오브 호러: -
플라이벤처: 140cm~195cm
회전목마: 100cm 이상
매직 붕붕카: 110cm~140cm'''


def allowedrides(height):
    assert type(height) == int

    result = [] 
    for ride in rides.splitlines():
        ridename, cmmin, cmmax = ridereader.read(ride)
        if (not cmmin and not cmmax) or (height >= cmmin and not cmmax) or (cmmin <= height <= cmmax):
            result.append(ridename)
    
    return result


if __name__ == "__main__":
    height = int(input())
    for x in allowedrides(height):
        print(x)