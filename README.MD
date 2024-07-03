# HoYoGames Autorun

Программа для автозапуска ваших Hoyoverse игр 

## Содержание
- [Библиотеки](#библиотеки)
- [Начало работы](#начало-работы)
  - [Для windows](#Windows)
  - [Для Linux](#Linux)
- [Deploy](#deploy)
- [License](#license)
- [Автор проекта](#author)

## Библиотеки

* flet
* PyAutoGUI
* PyGetWindow

## Начало работы

1. Скопируйте репозиторий
2. Создайте и активируйте ваше виртуально пространство
    ### Windows:
    ```commandline
    python -m venv venv
    source venv/Scripts/activate
    ```
    ### Linux:
    ```commandline
    python -m venv venv
    source venv/bin/activate
    ``` 
3. Установите зависимости
    ```commandline
    pip install -r requirements.txt
    ```

## Deploy
Для того чтобы скомпилировать программу в .exe файл используйте 
[pyinstaller](https://pyinstaller.org/en/stable/) 
или [flutter](https://flet.dev/docs/publish)

## License
Распространяется под лицензией MIT.\
Дополнительную информацию можно найти в файле `LICENSE.txt`.

## Author
* [pOsdas](https://github.com/pOsdas)