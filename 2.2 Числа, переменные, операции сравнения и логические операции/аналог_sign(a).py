# В некоторых языках есть функция sign(a), которая возвращает −1, если
# аргумент a отрицательный, и 1, если аргумент a положительный. В Python та-
# кой функции нет, но в модуль math включена функция math.copysign(x, y),
# которая возвращает абсолютное значение x со знаком y. Как можно было бы
# использовать эту функцию способом, аналогичным использованию отсутству-
# ющей функции sign(a)?
import math
a = float(input('введи число ублюдок и мы определим его знак'))
def sign (a):
        return int(math.copysign(a,a)/math.copysign(a,1))
print(sign(a))
