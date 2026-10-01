#!/bin/bash
# MSLightBrowser Complete Installation for Linux
# Automatically detects distribution and sets up everything

echo "========================================"
echo "MSLightBrowser - Complete Linux Setup"
echo "========================================"
echo ""

# Detect Linux distribution
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
    OS_NAME=$NAME
    echo "Detected: $OS_NAME"
else
    echo "❌ Could not detect your Linux distribution"
    exit 1
fi

echo ""
echo "📦 Installing dependencies..."
echo ""

# Install dependencies based on distribution
case $OS in
    ubuntu|debian)
        echo "Installing for Debian/Ubuntu..."
        sudo apt update
        sudo apt install -y python3.10 python3.10-venv python3.10-dev
        sudo apt install -y qt5-qmake qtbase5-dev libqt5webengine5
        sudo apt install -y git
        ;;
    fedora)
        echo "Installing for Fedora..."
        sudo dnf install -y python3.10 python3.10-devel
        sudo dnf install -y qt5-qtbase qt5-qtwebengine
        sudo dnf install -y git
        ;;
    rhel|centos)
        echo "Installing for RHEL/CentOS..."
        sudo dnf install -y python3.10 python3.10-devel
        sudo dnf install -y qt5-qtbase qt5-qtwebengine
        sudo dnf install -y git
        ;;
    arch)
        echo "Installing for Arch Linux..."
        sudo pacman -S --noconfirm python python-venv
        sudo pacman -S --noconfirm qt5-base qt5-webengine
        sudo pacman -S --noconfirm git
        ;;
    opensuse*)
        echo "Installing for openSUSE..."
        sudo zypper install -y python310 python310-venv python310-devel
        sudo zypper install -y libqt5-qtbase libqt5-qtwebengine
        sudo zypper install -y git
        ;;
    *)
        echo "⚠️  Unknown distribution: $OS"
        echo "Please install dependencies manually:"
        echo "   - Python 3.10+"
        echo "   - Qt 5.15+"
        echo "   - qtwebengine"
        read -p "Continue anyway? (y/n) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
        ;;
esac

echo ""
echo "✅ Dependencies installed"
echo ""

echo "📦 Setting up Python virtual environment..."
echo ""

# Create virtual environment
if command -v python3.10 &> /dev/null; then
    python3.10 -m venv .venv
elif command -v python3 &> /dev/null; then
    python3 -m venv .venv
else
    python -m venv .venv
fi

echo "✅ Virtual environment created"
echo ""

# Activate and install Python packages
echo "📦 Installing Python packages..."
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
echo "✅ Python packages installed"
echo ""

# Setup desktop entry
echo "========================================"
echo "Setting up desktop shortcuts..."
echo "========================================"
echo ""

bash setup-desktop-auto.sh

echo ""
echo "========================================"
echo "✅ Installation Complete!"
echo "========================================"
echo ""
echo "🎉 MSLightBrowser is ready to use!"
echo ""
echo "🚀 To launch:"
echo "   1. Open Activities menu (top-left)"
echo "   2. Search 'MSLightBrowser'"
echo "   3. Click to launch"
echo ""
echo "   OR double-click the desktop icon"
echo ""
echo "💡 Tip: You can also launch from terminal:"
echo "   $ cd $(pwd)"
echo "   $ source .venv/bin/activate"
echo "   $ python main.py"
echo ""
echo "⚠️  If icon doesn't appear:"
echo "   - Wait a few seconds"
echo "   - Press Alt+F2, type 'r', press Enter"
echo "   - Or log out and log back in"
echo ""
