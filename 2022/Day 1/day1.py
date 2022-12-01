import pandas as pd
import os

path = "C:/Users/Elton/Documents/GitHub/adventofcode/2022/Day 1"

os.chdir(path)

def solve1(path):
    with open(path+"/input1.csv") as file:
        data = file.read().splitlines()

        elf_num = 1
        elf_tot = 0
        elf_dic = {}

        for item in data:
            if item == '':
                elf_dic[elf_num] = elf_tot
                elf_num += 1
                elf_tot = 0
            else:
                elf_tot += int(item)

        elf_dic[elf_num] = elf_tot

    return (max(elf_dic, key=elf_dic.get), max(elf_dic.values()))


def solve2(path):
    with open(path+"/input1.csv") as file:
        data = file.read().splitlines()

        elf_num = 1
        elf_tot = 0
        elf_dic = {}

        for item in data:
            if item == '':
                elf_dic[elf_num] = elf_tot
                elf_num += 1
                elf_tot = 0
            else:
                elf_tot += int(item)

        elf_dic[elf_num] = elf_tot

    sorted_list = list(elf_dic.values())
    sorted_list.sort(reverse=True)

    return sum(sorted_list[:3])

print(solve2(path))
