from random import randint
al = [randint(0, 500), randint(0, 500), randint(0, 500), randint(0, 500), randint(0, 500)]
al.sort()
print('O menor número é {} e o maior é {}'.format(al[0], al[4]))
print(al)
