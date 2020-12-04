import json  # подключили библиотеку для работы с json
from pprint import pprint  # подключили Pprint для красоты выдачи текста

with open('json/dich.json', 'r',
          encoding='utf-8') as f:  # открыли файл с данными
    text = json.load(f)  # загнали все, что получилось в переменную
    pprint(text)  # вывели результат на экран
    s = []
    for i in text["datas"].keys():
        print("ver", i)
        for j in (text["datas"][i].items()):
            s.append([i, j[0], j[1]])
    print(s)




