"""
Meshtastic Linux Client Launcher

Launches the main PyQt6-based Meshtastic Linux Client GUI.
"""

import sys
from PyQt6 import QtWidgets
from ui.main_window import MainWindow

def main():
    """Main entry point."""
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

