"""
Aerospace theme stylesheet for OrbiHub
"""

AEROSPACE_THEME = """
/* Main Window */
QMainWindow {
    background-color: #F5F7FA;
}

/* Title Bar */
QLabel#titleLabel {
    background-color: #0B3D91;
    color: white;
    font-size: 24px;
    font-weight: bold;
    padding: 15px;
    border-bottom: 3px solid #E8B923;
}

/* Sidebar */
QPushButton#homeButton,
QPushButton#toolsButton,
QPushButton#settingsButton {
    background-color: #1C2541;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 20px;
    margin: 5px;
}

QPushButton#homeButton:hover,
QPushButton#toolsButton:hover,
QPushButton#settingsButton:hover {
    background-color: #0B3D91;
    border: 2px solid #E8B923;
}

QPushButton#homeButton:pressed,
QPushButton#toolsButton:pressed,
QPushButton#settingsButton:pressed {
    background-color: #E8B923;
}

/* Scroll Area */
QScrollArea {
    background-color: #F5F7FA;
    border: none;
}

/* Search Bar */
QLineEdit#searchLineEdit {
    background-color: white;
    border: 2px solid #0B3D91;
    border-radius: 8px;
    padding: 10px;
    font-size: 14px;
}

QLineEdit#searchLineEdit:focus {
    border: 2px solid #E8B923;
}

QPushButton#searchButton {
    background-color: #0B3D91;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: bold;
    font-size: 14px;
}

QPushButton#searchButton:hover {
    background-color: #E8B923;
    color: #1C2541;
}

/* Menu Bar */
QMenuBar {
    background-color: #1C2541;
    color: white;
    padding: 5px;
}

QMenuBar::item {
    background-color: transparent;
    padding: 5px 10px;
}

QMenuBar::item:selected {
    background-color: #0B3D91;
}

QMenu {
    background-color: #1C2541;
    color: white;
    border: 1px solid #0B3D91;
}

QMenu::item:selected {
    background-color: #0B3D91;
}

/* Status Bar */
QStatusBar {
    background-color: #1C2541;
    color: white;
}
"""