# MSLightBrowser 🚀

**Ультралегкий и быстрый браузер для повседневного использования.** Проект создан как практическая основа для браузера, который сочетает:

- низкое потребление памяти и CPU;
- быстрый старт и простой интерфейс;
- современные сетевые протоколы и криптографию, которые зависят от браузерного движка;
- максимальную совместимость с современными сайтами.

## Ключевая идея

Это не "самописный рендерер с нуля". Гораздо разумнее и надёжнее использовать проверенный браузерный движок, который уже поддерживает современные стандарты веба, TLS, HTTP/2 и HTTP/3, а также безопасную работу с сертификатами и шифрованием. Поэтому в проекте используется **QtWebEngine**, основанный на **Chromium**.

Это даёт:

- поддержку современных сайтов и JavaScript;
- безопасные соединения через TLS 1.3;
- корректную работу с SSL/TLS и сертификатами;
- быструю загрузку страниц и стабильную совместимость.

## Функции

✅ **Вкладки (Tabs)** — работа с несколькими сайтами одновременно  
✅ **Адресная строка** — автоматическое добавление https://  
✅ **Навигация** — кнопки назад/вперёд/обновить  
✅ **Блокировка рекламы** — фильтрация рекламных доменов  
✅ **Тёмная тема** — встроенная поддержка тёмного режима  
✅ **Приватность** — очистка истории, cookies, кеша  
✅ **Домашняя страница** — быстрый доступ к нужным сайтам  
✅ **Совместимость** — работает со всеми современными веб-приложениями  

## Требования

- **Python 3.10+**
- **Qt 5.15+** (с QtWebEngine)
- **ОС**: Windows, Linux, macOS

---

# Установка и запуск

## Windows 🪟

### Вариант 1: Автоматическая установка (рекомендуется)

1. **Скачайте репозиторий**
   ```bash
   git clone https://github.com/mars74da4p/MSLIghtBrowser.git
   cd MSLIghtBrowser
   ```

2. **Запустите install.bat**
   ```bash
   install.bat
   ```
   Скрипт автоматически установит Python (если его нет) и все зависимости.

3. **Запустите браузер**
   ```bash
   run.bat
   ```

### Вариант 2: Ручная установка

1. **Установите Python 3.10+**
   - Скачайте с [python.org](https://www.python.org/downloads/)
   - При установке отметьте "Add Python to PATH"

2. **Откройте Command Prompt (cmd) и выполните:**
   ```bash
   git clone https://github.com/mars74da4p/MSLIghtBrowser.git
   cd MSLIghtBrowser
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   python main.py
   ```

3. **Создайте ярлык для быстрого запуска** (опционально)
   - Создайте файл `launch.cmd` в папке проекта:
     ```batch
     @echo off
     .venv\Scripts\python.exe main.py
     pause
     ```
   - Кликните правой кнопкой на `launch.cmd` → "Send to" → "Desktop (create shortcut)"

---

## Linux 🐧

### Debian/Ubuntu

1. **Обновите пакеты и установите зависимости:**
   ```bash
   sudo apt update
   sudo apt install -y python3.10 python3.10-venv python3.10-dev
   sudo apt install -y qt5-qmake qtbase5-dev libqt5webkit5 libqt5webengine5
   sudo apt install -y git
   ```

2. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/mars74da4p/MSLIghtBrowser.git
   cd MSLIghtBrowser
   ```

3. **Создайте виртуальное окружение и установите зависимости:**
   ```bash
   python3.10 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Запустите браузер:**
   ```bash
   python main.py
   ```

### Fedora/RHEL/CentOS

1. **Установите зависимости:**
   ```bash
   sudo dnf install -y python3.10 python3.10-devel
   sudo dnf install -y qt5-qtbase qt5-qtwebengine
   sudo dnf install -y git
   ```

2. **Клонируйте и установите:**
   ```bash
   git clone https://github.com/mars74da4p/MSLIghtBrowser.git
   cd MSLIghtBrowser
   python3.10 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   python main.py
   ```

### Arch Linux

1. **Установите пакеты:**
   ```bash
   sudo pacman -S python python-venv
   sudo pacman -S qt5-base qt5-webengine
   sudo pacman -S git
   ```

2. **Клонируйте и запустите:**
   ```bash
   git clone https://github.com/mars74da4p/MSLIghtBrowser.git
   cd MSLIghtBrowser
   python -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   python main.py
   ```

### openSUSE

1. **Установите зависимости:**
   ```bash
   sudo zypper install -y python310 python310-venv python310-devel
   sudo zypper install -y libqt5-qtbase libqt5-qtwebengine
   sudo zypper install -y git
   ```

2. **Установите проект:**
   ```bash
   git clone https://github.com/mars74da4p/MSLIghtBrowser.git
   cd MSLIghtBrowser
   python3.10 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   python main.py
   ```

### Создание ярлыка на рабочий стол (Linux)

1. **Создайте файл `mslightbrowser.desktop` в `/home/user/.local/share/applications/`:**
   ```bash
   mkdir -p ~/.local/share/applications
   nano ~/.local/share/applications/mslightbrowser.desktop
   ```

2. **Вставьте содержимое** (замените `/path/to/project` на реальный путь):
   ```ini
   [Desktop Entry]
   Type=Application
   Name=MSLightBrowser
   Comment=Lightweight and fast web browser
   Exec=/path/to/MSLIghtBrowser/.venv/bin/python /path/to/MSLIghtBrowser/main.py
   Icon=internet-web-browser
   Terminal=false
   Categories=Network;WebBrowser;
   ```

3. **Сделайте файл исполняемым:**
   ```bash
   chmod +x ~/.local/share/applications/mslightbrowser.desktop
   ```

4. **Обновите кеш приложений:**
   ```bash
   update-desktop-database ~/.local/share/applications/
   ```

Теперь браузер появится в меню приложений.

---

## macOS 🍎

1. **Установите Homebrew** (если не установлен):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Установите Python и Qt:**
   ```bash
   brew install python@3.10 qt@5
   ```

3. **Клонируйте и установите:**
   ```bash
   git clone https://github.com/mars74da4p/MSLIghtBrowser.git
   cd MSLIghtBrowser
   python3.10 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   python main.py
   ```

---

## Решение проблем

### Linux: ошибка "No module named PyQt5"
```bash
source .venv/bin/activate
pip install --upgrade pip setuptools
pip install -r requirements.txt
```

### Linux: ошибка "libGL.so.1: cannot open shared object file"
```bash
sudo apt install libgl1-mesa-glx libxkbcommon-x11-0
```

### Windows: ошибка о Python в PATH
- Переустановите Python и **отметьте "Add Python to PATH"**
- Или вручную добавьте Python в PATH через System → Environment Variables

### macOS: ошибка при установке PyQt5
```bash
pip install --upgrade pip
pip install PyQt5==5.15.10 --no-binary PyQt5
```

---

## Использование

### Вкладки
- **Ctrl+T** — новая вкладка
- **Ctrl+W** — закрыть текущую вкладку
- **Ctrl+Tab** — переключение вкладок

### Навигация
- **Ctrl+L** — фокус на адресную строку
- **Alt+Left** — назад
- **Alt+Right** — вперёд
- **Ctrl+R** — обновить

### Приватность
- **Ctrl+Shift+Delete** — открыть настройки очистки данных
- Очистите историю, cookies и кеш

### Блокировка рекламы
- Включена по умолчанию
- Фильтрует популярные рекламные домены
- Можно отключить в Settings

---

## Структура проекта

```
MSLIghtBrowser/
├── main.py                 # Точка входа
├── browser.py              # Главное окно браузера
├── tab_widget.py           # Виджет с вкладками
├── ad_blocker.py           # Блокировка рекламы
├── privacy.py              # Управление приватностью
├── dark_theme.py           # Тёмная тема
├── settings.py             # Параметры браузера
├── requirements.txt        # Зависимости
├── install.bat             # Установка для Windows
├── run.bat                 # Запуск для Windows
└── README.md               # Этот файл
```

---

## Технический стек

- **Python 3.10+** — язык программирования
- **PyQt5** — UI фреймворк
- **QtWebEngine** — браузерный движок (Chromium)
- **Modern Cryptography** — TLS 1.3, QUIC поддержка через QtWebEngine

---

## Лицензия

MIT — используйте как хотите!

---

## Контакт

Вопросы? Создавайте issues на [GitHub](https://github.com/mars74da4p/MSLIghtBrowser/issues).
