from random import randint


def num_in_range(minn,maxx,list1):
    list_index=[]
    for i in range(len(list1)):
        if minn<=list1[i]<=maxx:
            list_index.append(i)
    return list_index





list1=[randint(-100,100) for _ in range(20)]
minn=int(input('введите нижний предел: '))
maxx=int(input('введите верхний предел: '))
print(list1)
print(num_in_range(minn,maxx,list1))