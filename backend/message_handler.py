"""
Message Handler

Handles sending and receiving chat messages through Meshtastic.
"""

import asyncio
from threading import Thread

class MessageHandler:
    """Handles sending and receiving text messages."""

    def __init__(self, bluetooth_handler, chat_callback=None):
        """
        Initialize the MessageHandler.

        Args:
            bluetooth_handler (BluetoothHandler): Bluetooth connection handler
            chat_callback (function): callback to update UI on message receive
        """
        self.bluetooth_handler = bluetooth_handler
        self.chat_callback = chat_callback
        self.thread = None

    def send_text(self, message):
        """Send a text message."""
        if self.bluetooth_handler.interface:
            asyncio.run(self.bluetooth_handler.interface.sendText(message))

    def start_receiving(self):
        """Start listening for incoming messages."""
        if self.bluetooth_handler.interface:
            self.bluetooth_handler.interface.onReceive = self.handle_incoming
            if not self.thread:
                self.thread = Thread(target=self._run_forever)
                self.thread.daemon = True
                self.thread.start()

    def handle_incoming(self, packet, interface):
        """Process incoming message packets."""
        user = packet.get('fromId', 'Unknown')
        text = packet.get('decoded', {}).get('text', '')
        if self.chat_callback and text:
            display = f"📡 {user}: {text}"
            self.chat_callback(display)

    def _run_forever(self):
        """Keeps asyncio loop running in background."""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_forever()

