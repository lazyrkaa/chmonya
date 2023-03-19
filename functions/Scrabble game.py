# В настольную игру «Скрэббл» (Scrabble; есть русская версия «Эрудит»)
# играют на поле размером 15×15 клеток, строки которого обозначаются бук-
# вами (A–O), а столбцы – числами (1–15). Написать функцию, определяющую,
# умещается ли слово на игровом поле, если задана позиция его первой буквы
# как строка (например, 'G7'), переменная, указывающая расположение слова
# по горизонтали или по вертикали, и само слово.
import re
pos, h_or_v, word = (i for i in input().split() if i != ' ') #это ГЕНЕРАТОР
# [expr(variable) (функция) for variable(переменная) in iterable if condition(variable)]
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
numbers = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
nums = re.findall(r'\d+', pos) #ебать чета нашла в интернете, крутая штука
def fit(pos,h_or_v, word):
    """determines if a word fits"""
    if h_or_v == 'h':
                for j in range(len(numbers)):
                    if numbers[j] == nums[0]:
                        if (len(numbers) - j) >= len(word):
                            print('ok')
                        else:
                            print('fuck')
    if h_or_v == 'v':
        for i in pos:
            if not i.isdigit():
                for j in range(len(letters)):
                    if letters[j] == '{}'.format(i):
                        if (len(letters) - j) >= len(word):
                            print('ok')
                        else:
                            print('fuck')

fit(pos, h_or_v, word)
