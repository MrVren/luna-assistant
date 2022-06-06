#Поиск нечетких сравнений для более свободной формы разговора
from fuzzywuzzy import fuzz
from vocabulary import word_list


def recognize_cmd(task):
    RC = {'task': '', 'percent': 0}
    for c, v in word_list['cmds'].items():
        for x in v:
            vrt = fuzz.ratio(task, x)
            if vrt  > RC['percent']:
                RC['task'] = c
                RC['percent'] = vrt
                print(RC)
    return RC