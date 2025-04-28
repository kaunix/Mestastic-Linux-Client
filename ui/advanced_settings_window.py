"""
Advanced Settings Window

Provides access to radio transmission settings (power, interval, modem config).
"""

from PyQt6 import QtWidgets

class AdvancedSettingsWindow(QtWidgets.QWidget):
    """Window for advanced radio settings."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Radio Settings")
        self.resize(400, 400)
        self.setup_ui()

    def setup_ui(self):
        """Set up advanced settings UI."""
        layout = QtWidgets.QFormLayout()
        self.tx_power = QtWidgets.QSpinBox()
        self.tx_power.setRange(2, 23)
        self.broadcast_interval = QtWidgets.QSpinBox()
        self.broadcast_interval.setRange(1, 3600)
        layout.addRow("TX Power (dBm):", self.tx_power)
        layout.addRow("Broadcast Interval (s):", self.broadcast_interval)
        self.setLayout(layout)

