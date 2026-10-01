#!/bin/bash
# MSLightBrowser Auto-Setup for Linux
# This script automatically sets up the application for your system

echo "========================================"
echo "MSLightBrowser - Linux Auto Setup"
echo "========================================"
echo ""

# Detect Linux distribution
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
    echo "Detected OS: $OS"
else
    echo "Could not detect your Linux distribution"
    exit 1
fi

# Get project directory
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "Project directory: $PROJECT_DIR"
echo ""

# Make launch.sh executable
echo "🔧 Making launcher executable..."
chmod +x "$PROJECT_DIR/launch.sh"
chmod +x "$PROJECT_DIR/setup-desktop-auto.sh"

# Create applications directory
APP_DIR="$HOME/.local/share/applications"
mkdir -p "$APP_DIR"

echo "📝 Creating desktop entry..."

# Create .desktop file with correct path
DESKTOP_FILE="$APP_DIR/mslightbrowser.desktop"

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

# Update desktop database
echo "🔄 Updating application database..."
update-desktop-database "$APP_DIR" 2>/dev/null || true

# Create desktop shortcut if Desktop folder exists
if [ -d "$HOME/Desktop" ]; then
    echo "📌 Creating desktop shortcut..."
    cp "$DESKTOP_FILE" "$HOME/Desktop/mslightbrowser.desktop"
    chmod +x "$HOME/Desktop/mslightbrowser.desktop"
    echo "✅ Desktop shortcut created"
else
    mkdir -p "$HOME/Desktop"
    cp "$DESKTOP_FILE" "$HOME/Desktop/mslightbrowser.desktop"
    chmod +x "$HOME/Desktop/mslightbrowser.desktop"
    echo "✅ Desktop folder created and shortcut added"
fi

echo ""
echo "========================================"
echo "✅ Setup Complete!"
echo "========================================"
echo ""
echo "📌 How to launch MSLightBrowser:"
echo ""
echo "   OPTION 1 - Activities Menu:"
echo "   1. Click Activities (top-left)"
echo "   2. Search 'MSLightBrowser'"
echo "   3. Click to launch"
echo ""
echo "   OPTION 2 - Desktop Icon:"
echo "   Double-click the MSLightBrowser icon on your desktop"
echo ""
echo "   OPTION 3 - Terminal:"
echo "   $ $PROJECT_DIR/launch.sh"
echo ""
echo "⚙️  If icon doesn't appear in Activities menu:"
echo "   1. Press Alt+F2"
echo "   2. Type 'r' and press Enter"
echo "   3. Or log out and log back in"
echo ""
echo "📝 To run from terminal directly:"
echo "   $ cd $PROJECT_DIR"
echo "   $ source .venv/bin/activate"
echo "   $ python main.py"
echo ""
echo "⚠️  Wayland Warning (safe to ignore):"
echo "   If you see 'Ignoring XDG_SESSION_TYPE=wayland' - that's normal!"
echo "   The browser will still work fine with X11."
echo ""
