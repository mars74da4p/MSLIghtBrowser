#!/bin/bash
# Автоматическая установка ярлыка MSLightBrowser на рабочий стол и в меню приложений (Fedora/GNOME)

echo "========================================"
echo "MSLightBrowser Desktop Entry Setup"
echo "========================================"
echo ""

# Проверяем, находимся ли мы в правильной директории
if [ ! -f "main.py" ]; then
    echo "❌ Error: main.py not found!"
    echo "   Please run this script from the MSLIghtBrowser directory"
    exit 1
fi

# Получаем полный путь к проекту
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "📁 Project directory: $PROJECT_DIR"
echo ""

# Делаем launch.sh исполняемым
echo "🔧 Making launch.sh executable..."
chmod +x "$PROJECT_DIR/launch.sh"

# Создаём файл .desktop в ~/.local/share/applications/
echo "📝 Creating desktop entry..."

APP_DIR="$HOME/.local/share/applications"
mkdir -p "$APP_DIR"

DESKTOP_FILE="$APP_DIR/mslightbrowser.desktop"

# Создаём .desktop файл
cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=MSLightBrowser
Comment=Lightweight and fast web browser
Comment[ru]=Ультралегкий и быстрый веб-браузер

Exec=$PROJECT_DIR/launch.sh
Icon=web-browser

Terminal=false
Categories=Network;WebBrowser;Utility;
Keywords=web;browser;internet;
StartupNotify=true
X-GNOME-Autostart-enabled=true
EOF

echo "✅ Desktop entry created at: $DESKTOP_FILE"
echo ""

# Обновляем базу данных приложений
echo "🔄 Updating application database..."
update-desktop-database "$APP_DIR" 2>/dev/null || true

# Также копируем на рабочий стол (если существует)
if [ -d "$HOME/Desktop" ]; then
    echo "📌 Creating desktop shortcut..."
    cp "$DESKTOP_FILE" "$HOME/Desktop/mslightbrowser.desktop"
    chmod +x "$HOME/Desktop/mslightbrowser.desktop"
    echo "✅ Desktop shortcut created at: $HOME/Desktop/mslightbrowser.desktop"
else
    echo "ℹ️  Desktop folder not found (that's OK, app is in menu)"
fi

echo ""
echo "========================================"
echo "✅ Installation complete!"
echo "========================================"
echo ""
echo "ℹ️  How to use:"
echo "   1. Open Activities menu (top-left corner)"
echo "   2. Search for 'MSLightBrowser'"
echo "   3. Click to launch"
echo ""
echo "   Or click the icon on your Desktop if created."
echo ""
echo "🔧 Troubleshooting:"
echo "   If the browser doesn't appear in Activities:"
echo "   1. Wait a few seconds for the system to update"
echo "   2. Restart GNOME Shell: Press Alt+F2, type 'r', press Enter"
echo "   3. Or log out and log back in"
echo ""
