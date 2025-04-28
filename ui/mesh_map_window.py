"""
Mesh Map Window

Visualizes the connected Meshtastic mesh network topology.
"""

from PyQt6 import QtWidgets

class MeshMapWindow(QtWidgets.QWidget):
    """Window displaying mesh network map."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mesh Network Map")
        self.resize(600, 600)
        self.setup_ui()

    def setup_ui(self):
        """Set up mesh map visualization."""
        layout = QtWidgets.QVBoxLayout()
        self.map_canvas = QtWidgets.QLabel("Mesh Map Visualization Here (WIP)")
        layout.addWidget(self.map_canvas)
        self.setLayout(layout)

