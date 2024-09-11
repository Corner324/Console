# vshell

**vshell** — это эмулятор командной строки для работы с виртуальной файловой системой, упакованной в формате ZIP. Он поддерживает команды `pwd`, `ls`, `cd`, и `cat`, позволяя взаимодействовать с архивом как с файловой системой.

## Особенности

- Поддержка команд `pwd`, `ls`, `cd`, и `cat`.
- Работа с ZIP-архивами без необходимости их распаковки.
- Простой интерфейс командной строки.

## Установка

Для использования **vshell** просто клонируйте репозиторий и запустите `main.py`, передав путь к ZIP-архиву в качестве аргумента.

```bash
git clone https://github.com/Corner324/Console.git
cd Console
python main.py путь_к_файлу.zip
```

## Использование

После запуска **vshell** вы увидите командную строку, где можно использовать следующие команды:

- `pwd` — Показывает текущую директорию.
- `ls` — Отображает содержимое текущей директории.
- `cd <путь>` — Переходит в указанную директорию. Используйте `..` для перехода на уровень вверх.
- `cat <файл>` — Показывает содержимое указанного файла.
- `stop` — Завершает работу **vshell**.

### Примеры команд

- `pwd`  
  Выводит путь к текущей директории.

- `ls`  
  Выводит список файлов и директорий в текущей директории.

- `cd folder`  
  Переходит в директорию `folder`.

- `cat file.txt`  
  Показывает содержимое `file.txt`.

## Документация

Для получения более подробной информации о внутреннем устройстве и архитектуре проекта, обратитесь к исходному коду в репозитории.


## Лицензия

Этот проект лицензирован под MIT License. См. [LICENSE](LICENSE) для получения подробной информации.