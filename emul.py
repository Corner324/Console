import os

class Emul:
    # Конструктор 
    def __init__(self, zip):
        self.zip = zip
        self.namelist = zip.namelist()        # Список элементов архива
        self.currentDir = zip.namelist()[0]   # Актуальный путь
        self.rootDir = zip.namelist()[0]      # Корневой путь
        datalist = zip.infolist()             # Названия и время файлов
        self.infodict = {}                    # Создание словаря для файлов

        for data in datalist:
            if (data.is_dir()):
                self.infodict[data.filename[:-1]] = data
            else:
                self.infodict[data.filename] = data
        
        self.setNamePath = {}
        for name in self.namelist:
            if name == self.currentDir:
                 continue
            modules = cutPath(name)
            self.setNamePath[name] = modules

    # Просмотр содержимого директории
    def ls(self):
        catalog = self.chooseItemInDir(self.currentDir)
        print(*catalog, "\n", end='\n')

    # Получение списка вложеных элементов
    def chooseItemInDir(self, directory):
        partsPath = cutPath(directory)  # Элементы пути
        border = len(partsPath)         # Граница пути
        lastDir = partsPath[border-1]   # Последний элемент
        items = set()
        for key in self.setNamePath:
            choosenPath = self.setNamePath[key]
            if len(choosenPath) > border:
                if choosenPath[border-1] == lastDir:
                    modules = self.setNamePath[key]
                    items.add(modules[border])
        return items

    # Просмотр содержимого файла
    def catenate(self, path):
        try:
            dir = self.clearPatn(path)
        except Exception as e:
            print(e)
            return
        try:
            with self.zip.open(dir) as myfile:
                print(myfile.read())
        except Exception as e:
            print(f"{dir} is not file")

    # Перейти по директории
    def comeDirectory(self, path):

        if path == "/":
            self.currentDir = self.rootDir

        elif path == "..":
            path = self.currentDir
            parts = path.split("/")
            newPath = ''
            if len(parts) == 2:
                newPath = self.rootDir
            for i in range (len(parts)-2):
                newPath += parts[i] + '/'
            self.currentDir = newPath 

        else:
            try:
                dir = self.clearPatn(path)
                if (dir in self.namelist) and not "." in dir:
                    self.currentDir = dir
                else:
                    raise ValueError(f"Невозможно получить доступ '{dir}': Не найден файл или директория")
            except Exception as e:
                print(e)

    # Получаем прямой путь к файлу
    def clearPatn(self, path):
        dir = ''
        path = self.normalizePath(path)
        if path[0] == "/" and path[1:] in self.namelist:
            dir = path[1:]
        elif path[0] != "/":
            dir =  os.path.join(self.currentDir, path)
        else: 
            raise ValueError(f"Невозможно получить доступ '{path}': Не найден файл или директория")
        return dir

    # Нормализуем название файла для работы с архивом
    def normalizePath(self, path):
        if path[len(path)-1] != '/' and not "." in path:
            path += '/'
        return path

# Разбиваем путь на элементы списка
def cutPath(path):
    modules = []
    modules = path.split("/")
    if modules[len(modules)-1] == '':
        modules.pop()
    return modules