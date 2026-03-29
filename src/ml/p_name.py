fo = open("name.txt", "r", encoding='utf8')
file0 = fo.read()

f1 = open("fname.txt", "r", encoding='utf8')
file1 = f1.read()

f2 = open("lname.txt", "r", encoding='utf8')
file2 = f2.read()


def rname(word):
    flag = 0
    for i in file0.split('\n'):
        if word == i:
            flag = 1

    if flag == 1:
        return 0
    else:
        return 1


def fname(word):
    flag = 0
    for i in file1.split('\n'):
        if word == i:
            flag = 1
    if flag == 1:
        return 0
    else:
        return 1


def lname(word):
    flag = 0
    for i in file2.split('\n'):
        if word == i:
            flag = 1
    if flag == 1:
        return 0
    else:
        return 1

