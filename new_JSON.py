import json

def sort_and_top10(ob):
    new_mas = sorted(ob, key=lambda mas: mas[1])

    a = int(len(new_mas)) - 1

    p = 0

    print('top 10')

    while p != 10:
        print(new_mas[a])
        a -= 1
        p += 1


def counter(ob):
    mas4 = []

    for ind in ob:
        p = 0
        for i in mas4:
            if ind[0] != i[0]:
                continue
            else:
                p = 1
                break
        if p != 0:
            continue
        else:
            mas4.append(ind)

    sort_and_top10(mas4)


def add(ob):

    mas3 = []

    for ind in ob:
        a = [ind]
        a.append(ob.count(ind))
        mas3.append(a)

    counter(mas3)


def more_then_6(ob):
    mas2 = []
    for ind in ob:

        for temp in ind:
            if len(temp) > 6:
                mas2.append(temp)

    add(mas2)


def import_file(file):
    mas = []

    a = file['rss']
    b = a['channel']
    c = b['items']
    for descr in c:
        mas.append(descr['description'].split(' '))


    more_then_6(mas)

#begin
with open('newsafr.json','r',encoding='utf-8') as f:
    file = json.load(f)

import_file(file)
