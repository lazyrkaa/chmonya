# В настольную игру «Скрэббл» (Scrabble; есть русская версия «Эрудит»)
# играют на поле размером 15×15 клеток, строки которого обозначаются бук-
# вами (A–O), а столбцы – числами (1–15). Написать функцию, определяющую,
# умещается ли слово на игровом поле, если задана позиция его первой буквы
# как строка (например, 'G7'), переменная, указывающая расположение слова
# по горизонтали или по вертикали, и само слово.
pos, h_or_v, word = (i for i in input().split() if i != ' ') #это ГЕНЕРАТОР
# [expr(variable) (функция) for variable(переменная) in iterable if condition(variable)]
letters = 'ABCDE'
numbers = '12345'
def fit(pos,h_or_v, word):
    """determines if a word fits"""
    if h_or_v == 'h':
        for i in pos:
            if i.isdigit():
                if (len(numbers.split('{}'.format(i))[1])+1) >= len(word):
                    print('ok')
                else:
                    print('fuck')
    if h_or_v == 'v':
        for i in pos:
            if not i.isdigit():
                if (len(letters.split('{}'.format(i))[1])+1) >= len(word):
                    print('ok')
                else:
                    print('fuck')

fit(pos, h_or_v, word)
