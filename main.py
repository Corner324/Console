import zipfile
import sys
import emul

""""
   Разработать эмулятор командной строки vshell. 
В качестве аргумента vshell принимает образ файловой системы известного формата (tar, zip).

   Обратите внимание: программа должна запускаться прямо из командной строки, 
а файл с виртуальной файловой системой не нужно распаковывать у пользователя. 
В vshell должны поддерживаться команды pwd, ls, cd и cat. 
Ваша задача сделать работу vshell как можно более похожей на сеанс bash в Linux. 
Реализовать vshell можно на Python или других ЯП, но кроссплатформенным образом.
"""

def main():
    with zipfile.ZipFile(sys.argv[1], 'r') as zip:
        object = emul.Emul(zip)
        print("Доступные команды - pwd, ls, cd, cat, для выхода используйте - stop\n")
        while True:
            print(f"* {object.currentDir}", end=": ")
            commands = input().split()
            if commands[0] == "pwd":
                print(object.currentDir)
            elif commands[0] == "ls":
                object.ls(commands)
            elif commands[0] == "cd":
                object.comeDirectory(commands[1])
            elif commands[0] == "cat":
                object.catenate(commands[1])
            elif commands[0] == "stop":
                break
        
main()